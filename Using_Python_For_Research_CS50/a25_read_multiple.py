import os


def read_book(title_path):
    ''' 
    Read a book and return it as string.
    '''
    with open(title_path, "r", encoding="utf8") as file:
        text = file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


text = read_book("book.txt")
print(text)


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

word_counts = count_words(text)
print("Count words:", count_words(text))


def word_stats(count_words):
    '''
    Return number of unique words and word frequency.
    '''
    num_unique = len(count_words)
    counts = count_words.values()
    return (num_unique, counts)


print(word_stats(word_counts))


# book_dir = "./"
# # list files
# print(os.listdir(book_dir))

# text = read_book("book.txt")
# words_count = count_words(text)
# (num_unique, counts) = word_stats(count_words)
# print("Unique:", num_unique)
# print("Counts:", counts)

# import pandas as pd
# stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
# title_num = 1


# for book in os.listdir(book_dir):
#     # sub directory
#     for author in os.listdir(book_dir + "/" + language):
#         for title in os.listdir(book_dir + "/" + language + "/" + author):
#             inputfile = book_dir + "/" + language + "/" + author + "/" + title
#             print(inputfile)
#             text = read_book(inputfile)
#             (num_unique, counts) = word_stats(count_words(text))
#             stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique 
#             title_num += 1

# print(stats.head())


# import pandas as pandas
# stats = pd.Dataframe(columns = ("language", "author", "title", "length", "unique"))

# table = pd.Dataframe(columns = ("name", "age"))
# table.loc[1] = "James", 22
# table.loc[2] = "Jess", 29
# print(table.columns)

# print(stats.length)
# print(stats.unique)


# import matplotlib.pyplot as plt 

# # plt.plot(stats.length, stats.unique, "bo")
# # plt.show()

# plt.loglog(stats.length, stats.unique, "bo")
# plt.show()

# print(stats[stats.language == "English"])

# # plt.figure(figsize = (10, 10))
# # subset = stats[stats.language == "English"]
# # plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
# # subset = stats[stats.language == "French"]
# # plt.loglog(subset.length, subset.unique, "o", label = "French", color = "green")
# # plt.legend()
# # plt.xlabel("Book length")
# # plt.ylabel("Number of words")
# # plt.show()

