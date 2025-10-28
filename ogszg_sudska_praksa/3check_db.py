import sqlite3


# Path to your SQLite database file
db_path = 'dokumenti.db'  # or your actual filename


def main():
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    # Get total number of records in 'praksa' table
    cursor.execute("SELECT COUNT(*) FROM praksa")
    total_rows = cursor.fetchone()[0]


    # Get total number of inputs, assuming there's an 'inputs' table
    # Replace 'inputs' with your actual inputs table name
    try:
        cursor.execute("SELECT COUNT(*) FROM inputs")
        total_inputs = cursor.fetchone()[0]
    except sqlite3.Error:
        # If 'inputs' table doesn't exist, set to 0
        total_inputs = 0


    # Read the existing HTML content
    try:
        with open('html.html', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []


    # Prepare the first line with counts
    first_line = f"<p>Broj sudske praske u databazi: {total_rows}</p>\n"


    # Insert or replace the first line
    if lines:
        lines[0] = first_line
    else:
        lines.insert(0, first_line)


    # Write back the updated HTML
    with open('html.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)


    # Close the database connection
    conn.close()


if __name__ == '__main__':
    main()