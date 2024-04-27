"""
Performs in-place selection sort on the given array

Worst case time complexity: O(n^2);
    where n is the length of the input array
"""

def selection_sort(arr):
    n = len(arr)

    # go through each element in the array
    for i in range(n):
        # assume the current element is the minimum
        min_index = i

        # go through rest of the elements in the array
        # compare them with the current minimum element
        # update the minimun index if a smaller element is found
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the found minimum element with the element at current index
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# test
arr = [93, 18, 34, 20, 83, 58, 78, 12, 57, 37, 50, 33, 67, 28, 61, 77, 88, 52, 10, 92]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
        

        