
# string = "Python Programming"
# print(string[::-1])


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"
# count = 0
# for character in word:
#     if character in vowel:
#         count += 1
# print(count)


# word = "There is something above."
# dic = {}
# for key in word:
#     if key in dic:
#         dic[key] += 1
#     else:
#         dic[key] = 1
# print(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))


# fib = [0,1]
# for x in range(10):
#     fib.append(fib[-1] + fib[-2])
# print(fib)
# print(', '.join(str(x) for x in fib))


# lst = [4, 66, 3, 9, 13, 64]
# print("Maximum:", max(lst), "Minimum:", min(lst))


# lst = [4, 66, 3, 9, 13, 64]
# print(int(len(lst))/2)


# Join list element to string
# lst = ["P", "y", "t", "h", "o", "n"]
# string = ''.join(lst)
# print(string)


# Sum 2 lists
# lst = [1, 2, 3]
# lst2 = [4, 5, 6]
# sumlst = []
# for i in range(0, len(lst)):
#     sumlst.append(lst[i] + lst2[i])
# print(sumlst)


# Check if words are anagrams
# string = "bambus"
# string2 = "ousbam"
# if sorted(string) == sorted(string2):
#     print("String2 is anagram")
# else:
#     print("String2 is not anagram")


# Check for palindrome
# str = "nurses run"
# if str.replace(" ", "") == str[::-1].replace(" ", ""):
#     print("It is palindrome")
# else:
#     print("It is not palindrome")


# Counting white characters
# str = "There is some boat on the sea.\n And thats it."
# print(str)
# counter = 0
# for x in str:
#     if x.isspace():
#         counter += 1
# print(counter)


# Counting Digits, Letters, and Spaces in a String
# import re
# string = "There are: 22 boats on the sea!\n And thats it?"
# letters = len(re.findall("[a-zA-Z]", string))
# spaces = len(re.findall("[ ]", string))
# digits = len(re.findall("[0-9]", string))
# print("Letters:", letters, "Spaces:", spaces, "Digits:", digits)

# special_characters = ['.', ',', ':', ';', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '/', '\\', '-', '_', '&', '+',
#                         '-', '=', '|', ' ', '\t', '\n', '\r', '\f', '\v','\0', '\a', '\e', '\x1A', '\b']
# count = 0
# for x in string:
#     if x in special_characters:
#         count += 1
# print(count)

# special_characters2 = r'[.,:;?!\'\(\)\[\]{}\/*\-_&+\-=| \t\n\r\f\v\a\e\x1A\b]'
# x = len(re.findall(special_characters2, string))
# print(x)


# Counting Special Characters
import re
string = "And that's it?"
special_characters = r"[.,:;?!\'\(\)\[\]{}\/*\-_&+\-=| \t\n\r\f\v\a\x1A\b]"
special_characters_count = len(re.findall(special_characters, string))
print(special_characters_count)
