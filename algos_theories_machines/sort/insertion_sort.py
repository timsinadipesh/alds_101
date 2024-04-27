"""
Insertion sort

Worst case time complexity: O(n^2);
    where n is the length of the input array
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # compare the key to elements in the sorted array
        # move those that are greater than the key
        # one position ahead 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place the key in its correct position
        arr[j + 1] = key
    
    return arr


# usage
arr = [93, 18, 34, 20, 83, 58, 78, 12, 57, 37, 50, 33, 67, 28, 61, 77, 88, 52, 10, 92]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)