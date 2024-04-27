""" 
Exponential Search:

Jump search with exponential step size
Using binary search after identifying target block

Worst case time complexity: O(log n);
    where n is the length of the input array
"""

import random

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    i = 1
    # loop while i is less than the array length
    # and i is less than the target index
    # effectively finding the range for binary search
    while i < len(arr) and arr[i] < target:
        i *= 2
    
    # binary search within the found range
    return binary_search(arr, target, i//2, min(i, len(arr)))


def binary_search(arr, target, left_ind, right_ind):
    while left_ind <= right_ind:
        mid = left_ind + (right_ind - left_ind) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_ind = mid + 1
        else:
            right_ind = mid - 1
    return -1 # target not found


# usage
arr = [x for x in range(0, 20, random.randint(1, 3))]
target = random.randint(0, 19)
result = exponential_search(arr, target)

print(arr)
if result != -1:
    print(f"Element {target} is present at index: {result}")
else:
    print(f"Element {target} is not present in the array.")
