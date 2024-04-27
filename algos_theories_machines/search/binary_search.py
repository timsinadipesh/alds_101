"""
Performs binary search on a sorted array

Worst case time complexity: O(log n);
    where n is the length of the input array
"""

def binary_search(arr, target):
    # initialize pointers for the start and the end of the array
    left_ind, right_ind = 0, len(arr) - 1

    # continue searching until the left pointer is less then the right pointer
    while left_ind <= right_ind:
        mid = (left_ind + right_ind) // 2

        # return the index if the target is at that index
        if arr[mid] == target:
            return mid
        
        # if the target is less than the element at middle index, search the left half
        elif target < arr[mid]:
            right_ind = mid - 1

        # else search the right half
        else:
            left_ind = mid + 1

    # if target not found in the array, return -1
    return -1


# test
targets = [2, 5, 9, 11, 14, 38]
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

for target in targets:
    result = binary_search(arr, target)
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")