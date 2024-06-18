text = "This is test text. We are keeping this text short to keep things manageable. !Test text!"

def count_words(text):
    '''
    Count words in string and adds them to dictionary.
    '''
    text = text.lower()
    skip = [".", ",", "!", "?", "'", '"', ":", ";"]
    for char in skip:
        text = text.replace(char, "")
    word_count = {}
    for word in text.split(" "):
        # known word
        if word in word_count:
            word_count[word] += 1
        # unknown word
        else:
            word_count[word] = 1
    return word_count 

print(count_words(text))


# With collections library
from collections import Counter
def count_words_with_counter(text):
    '''
    Count words in string and adds them to dictionary.
    '''
    text = text.lower()
    skip = [".", ",", "!", "?", "'", '"', ":", ";"]
    for char in skip:
        text = text.replace(char, "")

    word_count = Counter(text.split(" "))
    return word_count

print(count_words_with_counter(text))


text = read_book("book.txt")

def read_book(title_path):
    ''' 
    Read a book and return it as string.
    '''
    with open(title_path, "r", encoding="utf8") as file:
        text = file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

print(read_book("book.txt"))



def word_stats(count_words):
    '''
    Return number of unique words and word frequency.
    '''
    num_unique = len(count_words)
    counts = count_words.values()
    return (num_unique, counts)

text = read_book("book.txt")
words_count = count_words(text)

(num_unique, counts) = word_stats(words_count)

print("Unique words: ", num_unique)
print("Total sum words: ", sum(counts))
