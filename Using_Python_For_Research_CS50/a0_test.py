map = {
    'a': 1,
    'b': 2,
    'c': 3
}

x = 'b'
y = map[x]

print(f'{x} -> {y}')
print(x, y)


def atuple(a, b):
    return (a, b)
result = atuple(3,5)
print(result)

from typing import Tuple
def create_tuple(a: int, b: int) -> Tuple[int, int]:
    return (a, b)
result = create_tuple(1, 2)
print(result) 

a = 3
b = a
print(b - 1)


import copy # Copies are used for nested objects, like list within list
q = [1,[2]]
w = copy.copy(q)
z = copy.deepcopy(q)
print("q is w", q is w)
print("q is z", q is z)
print("q == z", q == z)
print("q == w", q == w, q)
q.append(8)
q[1].append(23)
print("q is", q)
print("w is", w)
print("z is", z)


address_count = {'F': 1, 'o': 93, 'u': 21}
print(max(address_count.values()))
