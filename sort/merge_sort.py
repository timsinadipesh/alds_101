"""
Merge sort algorithm
Sorts an array in ascending order

Worst case time complexity: O(n log n); 
    where n is the length of the input array
"""

def merge_sort(arr):
    # base case: return the array if sorted
    if len(arr) <= 1:
        return arr
    
    # split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_ind, right_ind = 0, 0

    # compare two integers from both arrays
    # append the smallest one to the result array
    # update the index
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] <= right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1
        else:
            result.append(right[right_ind])
            right_ind += 1

    # add remaining arrays from left and right arrays
    result.extend(left[left_ind:])
    result.extend(right[right_ind:])

    return result


# usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)