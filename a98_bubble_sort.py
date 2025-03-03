
# Bubble sort

import pdb

def bubble_sort(arr):
    n = len(arr)
    #pdb.set_trace()
    for i in range(n - 1):
        
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
numbers = [64, 25, 12, 22, 11]
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
