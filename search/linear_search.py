"""
Linear Search

Worst case time complexity = O(n);
    where n is the length of the input array
"""

import random

def linear_search(arr, tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return -1


# usage
arr = [x for x in range(0, 10, random.randint(1, 3))]
target = random.randint(0, 9)
result = linear_search(arr, target)

print(arr)
if result != -1:
    print(f"Element {target} is present at index: {result}")
else:
    print(f"Element {target} is not present in the array.")
