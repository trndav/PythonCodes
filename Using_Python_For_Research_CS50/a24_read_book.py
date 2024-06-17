
def read_book(title_path):
    ''' 
    Read a book and return it as string.
    '''
    with open(title_path, "r", encoding="utf8") as file:
        text = file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

print(read_book("book.txt"))
