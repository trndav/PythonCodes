import os
import subprocess
import sys

# Paths to files and folders
file_to_delete_1 = 'dokumenti.db'
file_to_delete_2 = 'html.html'
folder_to_clean = 'Extracted_Sections'


# Scripts to run
current_dir = os.path.dirname(os.path.abspath(__file__))

script1 = os.path.join(current_dir, '1extract_from_docx.py')
script2 = os.path.join(current_dir, '2praksa_extract_add_to_db.py')
script3 = os.path.join(current_dir, '3check_db.py')


def delete_files():
    # Delete specific files if they exist
    for file_path in [file_to_delete_1, file_to_delete_2]:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path}")
        else:
            print(f"{file_path} does not exist, skipping deletion.")


    # Delete all files in the specified folder
    if os.path.exists(folder_to_clean) and os.path.isdir(folder_to_clean):
        for filename in os.listdir(folder_to_clean):
            file_path = os.path.join(folder_to_clean, filename)
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        print(f"Folder {folder_to_clean} does not exist or is not a directory.")


def run_script(script_path):
    print(f"Running {script_path}...")
    process = subprocess.run([sys.executable, script_path], check=True)
    print(f"{script_path} completed.")


def main():
    delete_files()
    run_script(script1)
    run_script(script2)
    run_script(script3)
    print("All tasks completed successfully.")


if __name__ == "__main__":
    main()