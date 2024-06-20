import os

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


def word_stats(count_words):
    '''
    Return number of unique words and word frequency.
    '''
    num_unique = len(count_words)
    counts = count_words.values()
    return (num_unique, counts)


book_dir = "./"
# list files
print(os.listdir(book_dir))

import pandas as pandas
stats = pd.Dataframe(columns = ("language", "author", "title", "length", "unique"))
title_num = 1


for book in os.listdir(book_dir):
    # sub directory
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique 
            title_num += 1

print(stats.head())

import pandas as pandas
stats = pd.Dataframe(columns = ("language", "author", "title", "length", "unique"))

table = pd.Dataframe(columns = ("name", "age"))
table.loc[1] = "James", 22
table.loc[2] = "Jess", 29
print(table.columns)
