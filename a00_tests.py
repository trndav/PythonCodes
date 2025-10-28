# # size = 5
# # fill_ratio = 0.30

# # def generate_board(size, fill_ratio):
# #     board = [['.' for _ in range(size)] for _ in range(size)]
# #     return board
# # print(generate_board(size, fill_ratio))


# # def is_palindrome(x):
# #     x = x.replace(" ", "").lower()
# #     b = x[::-1].lower().replace(" ", "")
# #     if x == b:
# #         print(True)
# # is_palindrome("Never odd or even") #→ True

# #a = "bom"
# # print(a[::-1])

# # Given a list of numbers, return a list of all numbers that are greater than the average.
# # def above_average(lst):
# #     x = sum(lst) / len(lst)
# #     a = []
# #     for i in lst:
# #         if i > x:
# #             a.append(i)
# #     print(a)    
# # above_average([1,2,3,4,5]) # → [4,5]

# # Write a function that returns the first non-repeating character in a string, or None if all repeat.
# def first_unique(s):
#     counts = {}
#     for i in s:
#         counts[i] = counts.get(i, 0) + 1
#     for i in s:
#         if counts[i] == 1:
#             return i
# print(first_unique("aabbccde")) #→ 'd'

# def first_unique(s):
#     for i in s:
#         if s.index(i) == s.rindex(i):
#             return i
# print(first_unique("aabbccde")) #→ 'd'


# person = {"name": "Alice", "age": 25}
# person["city"] = "Paris"
# print(person)

# person.update({"job": "Engineer", "hobby": "Painting"})
# print(person)
from datetime import datetime

# date_string = "04/02/2025"
# date_object = datetime.strptime(date_string, "%m/%d/%Y")
# print(date_object)  # 2025-04-02 00:00:00

def transform_date_format(dates):
    date_object = datetime.strptime(dates, "%m/%d/%Y")
    return [date_object]

if __name__ == "__main__":
    dates = transform_date_format(["2010/02/20", "2 016p 19p 12", "11-18-2012", "2018 12 24", "20130720"])
    print(*dates, sep='\n')