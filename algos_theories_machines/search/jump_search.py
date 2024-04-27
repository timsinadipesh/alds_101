"""
Jump Search

Time complexity depends on the step size
Here:
Worst case time complexity: O(sqrt(n));
    where n is the length of the input array
"""

import math
import random

def jump_search(arr, target):
    n = len(arr)
    # determine the size of the jump
    step = int(math.sqrt(n))

    # find the block that could contain the target
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: # element not found
            return -1 

    # linear search within the possible target block
    if arr[prev] < target:
        prev += 1
        if prev == min(step, n): # we reach the end of the block
            return -1 

    if arr[prev] == target:
        return prev

    return -1 


# usage
arr = [x for x in range(0, 10, random.randint(1, 3))]
target = random.randint(0, 9)
result = jump_search(arr, target)

print(arr)
if result != -1:
    print(f"Element {target} is present at index: {result}")
else:
    print(f"Element {target} is not present in the array.")