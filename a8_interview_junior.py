
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


lst = ["P", "y", "t", "h", "o", "n"]
string = ''.join(lst)
print(string)