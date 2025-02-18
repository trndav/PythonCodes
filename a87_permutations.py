

from itertools import permutations, product
items = ['A', 'B', 'C', 'D']

# Permutations without repeat
# #perms = list(permutations(items, 4))
# perms = [''.join(p) for p in permutations(items, 3)]  # Pick 2 at a time
# print(perms)

# Letters can repeat
perms = [''.join(p) for p in product(items, repeat=3)]  # Allow repetitions
print(perms)
