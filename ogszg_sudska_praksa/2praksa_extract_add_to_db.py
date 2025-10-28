import os
import sqlite3
from bs4 import BeautifulSoup
from docx import Document


# Path to your directory containing Word documents
directory_path = 'Extracted_Sections'


# Path to your SQLite database file
db_path = 'dokumenti.db'


# Define the database schema
CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS praksa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    source TEXT,
    about TEXT,
    content TEXT
)
'''


def parse_document_with_formatting(file_path):
    try:
        # Read document and convert to HTML lines
        doc = Document(file_path)
        html_paragraphs = []


        for paragraph in doc.paragraphs:
            paragraph_html = ""
            for run in paragraph.runs:
                run_text = run.text
                if not run_text:
                    continue
                if run.bold:
                    run_text = f"<b>{run_text}</b>"
                if run.underline:
                    run_text = f"<u>{run_text}</u>"
                if run.italic:
                    run_text = f"<i>{run_text}</i>"
                paragraph_html += run_text
            html_paragraphs.append(f"<p>{paragraph_html}</p>")


        full_html = "\n".join(html_paragraphs)
        soup = BeautifulSoup(full_html, 'html.parser')


        lines_html = [str(element) for element in soup.find_all(['p', 'li'])]


        lines = lines_html


        # Initialize variables
        name_html = ''
        source_html = ''
        remaining_lines = []


        # Handle the first line
        if lines:
            first_line_soup = BeautifulSoup(lines[0], 'html.parser')
            first_line_text = first_line_soup.get_text().strip()


            import re
            if re.match(r'^\d+\.', first_line_text):
                # Skip numbered line
                lines = lines[1:]
                if lines:
                    name_html = lines[0]
                    lines = lines[1:]
                else:
                    name_html = ''
            else:
                name_html = lines[0]
                lines = lines[1:]
        else:
            name_html = ''


        # Extract source: the first non-empty line after the name
        source_start_index = -1
        source_end_index = -1
        source_found = False
        source_text = ''


        for idx, line in enumerate(lines):
            line_soup = BeautifulSoup(line, 'html.parser')
            text_line = line_soup.get_text().strip()
            if text_line:
                # First non-empty line is source
                source_html = f"<p>{text_line}</p>"
                source_start_index = idx
                source_found = True
                break


        if source_found:
            # Find the index where source ends: first line starting with '-'
            for idx in range(source_start_index + 1, len(lines)):
                line_soup = BeautifulSoup(lines[idx], 'html.parser')
                text_line = line_soup.get_text().strip()
                if text_line.startswith('-'):
                    source_end_index = idx
                    break
            else:
                source_end_index = source_start_index + 1  # If no dash, source ends at next line


        # Collect source lines
        source_lines = lines[source_start_index:source_end_index]
        if source_lines:
            source_html = ''.join(source_lines)


        # Store source text for comparison
        source_soup = BeautifulSoup(source_html, 'html.parser')
        source_text = source_soup.get_text().strip()


        # Remaining lines after source
        remaining_lines = lines[source_end_index:] if source_found else []


        about_lines = []
        content_lines = []


        # Collect about lines based on rules:
        # - Lines starting with '-' OR containing bold are part of About
        # - The About section ends when a line does NOT start with '-' AND does NOT contain bold
        about_active = True


        for line in remaining_lines:
            line_soup = BeautifulSoup(line, 'html.parser')
            text_line = line_soup.get_text().strip()


            # Skip duplicate source line
            if text_line == source_text:
                continue


            starts_with_dash = text_line.startswith('-')
            contains_bold = bool(line_soup.find(['b', 'strong']))


            if about_active:
                if starts_with_dash or contains_bold:
                    about_lines.append(line)
                else:
                    # End of About section
                    about_active = False
                    content_lines.append(line)
            else:
                content_lines.append(line)


        # Wrap in <p> tags if not empty
        about_html = ''.join(about_lines).strip()
        content_html = ''.join(content_lines).strip()


        about_html = f"<p>{about_html}</p>" if about_html else ''
        content_html = f"<p>{content_html}</p>" if content_html else ''


        return {
            'name': name_html,
            'source': source_html,
            'about': about_html,
            'content': content_html
        }


    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None
   
def main():
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    # Create table if not exists
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()


    # Iterate through all Word documents
    for filename in os.listdir(directory_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing: {filename}")
            record = parse_document_with_formatting(file_path)
            if record:
                # Insert into database
                cursor.execute('''
                    INSERT INTO praksa (name, source, about, content)
                    VALUES (?, ?, ?, ?)
                ''', (record['name'], record['source'], record['about'], record['content']))
                conn.commit()


    # Close connection
    conn.close()
    print("All documents processed and stored in the database.")


if __name__ == '__main__':
    main()