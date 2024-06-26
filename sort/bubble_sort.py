""" 
Bubble sort

Worst case time complexity: O(n^2); 
    where n is the length of the input array 
"""

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # flag to track swapping in the current iteration
        swapped = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # place the larger element in the higher index position
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        # if no swapping occurred, the array is already sorted
        if not swapped:
            break

    return array

# usage
arr = [93, 18, 34, 20, 83, 58, 78, 12, 57, 37, 50, 33, 67, 28, 61, 77, 88, 52, 10, 92]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)