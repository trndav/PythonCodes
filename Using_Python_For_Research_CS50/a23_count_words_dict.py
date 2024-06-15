# Needs improvement, to count words which end with .,!? 

test = "This is test text We are keeping this text short to keep things manageable."

def count_words(text):
    '''
    Count words in string and adds them to dictionary.
    '''
    word_count = {}
    for word in text.split(" "):
        # known word
        if word in word_count:
            word_count[word] += 1
        # unknown word
        else:
            word_count[word] = 1
    return word_count 

count_words(text)
