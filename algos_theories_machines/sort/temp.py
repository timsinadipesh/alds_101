


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