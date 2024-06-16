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
