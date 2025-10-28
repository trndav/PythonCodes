from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from bs4 import BeautifulSoup
import os
from docx import Document
from markupsafe import Markup


app = Flask(__name__)


# Path to store uploaded files temporarily
UPLOAD_FOLDER = 'Dokumenti'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Your existing parsing function (make sure to include it here)
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


        # Extract source from remaining lines
        for line in lines:
            line_soup = BeautifulSoup(line, 'html.parser')
            text_line = line_soup.get_text().strip()
            if text_line:
                source_html = f"<p>{text_line}</p>"
                break


        # Find index of source line
        source_index = lines.index(source_html) if source_html in lines else -1
        # Remaining lines after source are for about/content
        remaining_lines = lines[source_index+1:] if source_index != -1 else lines


        # Store the source text for comparison
        source_text = ''
        if source_html:
            source_soup = BeautifulSoup(source_html, 'html.parser')
            source_text = source_soup.get_text().strip()


        about_lines = []
        content_lines = []


        about_active = True


        for i, line in enumerate(remaining_lines):
            line_soup = BeautifulSoup(line, 'html.parser')
            text_line = line_soup.get_text().strip()


            # Check if line is the source to exclude it from About
            if text_line == source_text:
                continue  # Skip adding source to About


            starts_with_dash = text_line.startswith('-')
            contains_bold = bool(line_soup.find(['b', 'strong']))


            if about_active:
                if starts_with_dash or contains_bold:
                    about_lines.append(line)
                else:
                    about_active = False
                    content_lines.extend(remaining_lines[i:])
                    break
            else:
                content_lines.extend(remaining_lines[i:])


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


# Database path
DATABASE = '../dokumenti.db'  # Adjust as needed


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    total_rows = conn.execute('SELECT COUNT(*) FROM praksa').fetchone()[0]


    search_query = ''
    results = []
    search_performed = False


    if request.method == 'POST':
        search_query = request.form.get('keyword', '').strip()
        if search_query:
            sql = '''
                SELECT * FROM praksa
                WHERE name LIKE ? OR source LIKE ? OR about LIKE ? OR content LIKE ?
            '''
            like_pattern = f'%{search_query}%'
            results = conn.execute(sql, (like_pattern, like_pattern, like_pattern, like_pattern)).fetchall()
            search_performed = True


    conn.close()
    return render_template('index.html', total_rows=total_rows, results=results, keyword=search_query, search_performed=search_performed)


@app.route('/content/<int:pr_id>')
def content(pr_id):
    keyword = request.args.get('keyword', '')
    conn = get_db_connection()
    record = conn.execute('SELECT * FROM praksa WHERE id = ?', (pr_id,)).fetchone()
    conn.close()
    if record:
        return render_template('content.html', record=record, keyword=keyword)
    else:
        return "Record not found", 404


# Upload 1 docx
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    message = ''
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.docx'):
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)


            # Parse the document
            record = parse_document_with_formatting(filepath)


            # Insert into database
            if record:
                conn = get_db_connection()
                conn.execute('''
                    INSERT INTO praksa (name, source, about, content)
                    VALUES (?, ?, ?, ?)
                ''', (record['name'], record['source'], record['about'], record['content']))
                conn.commit()
                conn.close()


            # Remove the uploaded file
            os.remove(filepath)


            message = 'Dokument je dodan u sudsku praksu.'
            return render_template('upload.html', success=True, message=message)


        else:
            message = 'Dokument nije učitan. Provjerite da li je dokument u .docx formatu.'


    return render_template('upload.html', message=message)


# Highlight keyword filter
@app.template_filter('highlight')
def highlight(text, search):
    if not search:
        return text
    import re
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    highlighted_text = pattern.sub(f"<span style='background-color: yellow;'>{search}</span>", text)
    return Markup(highlighted_text)


if __name__ == '__main__':
    # Create table if not exists
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS praksa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            source TEXT,
            about TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()


    app.run(host='0.0.0.0', port=5000)