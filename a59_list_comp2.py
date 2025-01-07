# Comprehension lists

a = [1, 2, 3, 4, 5, 6, 7, 8]
f = [x*x for x in a if x % 2 == 0]
print(f)

b = [1, 2, 3, 4, 5, 6, 7, 8]
c = [x*x if x % 2 == 0 else x for x in b]
print(c)

words = ["apple", "is", "a", "fruit"]
three = [x for x in words if len(x) <= 3]
print(three)

nested_list = [[1, 2], [3, 4], [5, 6]]
flat = [x for y in nested_list for x in y]
print(flat)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combine = [list1 + list2]
# print(combine)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
odd_products = [x * y for x in list1 for y in list2 if (x * y) % 2 != 0]
print(odd_products)
