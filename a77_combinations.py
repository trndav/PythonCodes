from itertools import combinations, permutations, product

letters = ['A', 'B', 'C', 'D']
combo = list(combinations(letters, 2))  
print(combo)

combo2 = list(permutations(letters, 2)) 
print(combo2)

combo3 = list(product(letters, repeat=2))  
print(combo3)