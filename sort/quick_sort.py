"""
Quick sort

Worst case time complexity: O(n^2);
    where n is the length of the input array
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
    
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + [pivot] + quick_sort(right)


# usage
arr = [93, 18, 34, 20, 83, 58, 78, 12, 57, 37, 50, 33, 67, 28, 61, 77, 88, 52, 10, 92]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)