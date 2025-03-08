from collections import Counter
from docx import Document

def count_correct_answers(docx_file):
    doc = Document(docx_file)
    answer_counts = Counter()
    total_questions = 0

    for para in doc.paragraphs:
        text = para.text.strip()
        
        # Check if paragraph contains a multiple-choice answer
        if text and any(text.startswith(f"{opt})") for opt in "abcd"):
            # Detect correct answer (indented answer)
            if para.paragraph_format.first_line_indent or para.paragraph_format.left_indent:
                correct_answer = text[0]  # Get 'a', 'b', 'c', or 'd'
                answer_counts[correct_answer] += 1
                total_questions += 1

    # Calculate percentages
    if total_questions == 0:
        print("No valid questions found.")
        return
    
    print("Correct Answer Distribution:")
    for answer, count in answer_counts.items():
        percentage = (count / total_questions) * 100
        print(f"{answer.upper()}: {percentage:.2f}%")

# Example usage
docx_file = "PITANJA_SA_DRZAVNOG_ISPITA.docx" 
count_correct_answers(docx_file)
