"""
Quicksort is a divide and conquer algorithm.
Quicksort first divides a large array into two smaller
sub-arrays: the low elements and the high elements.
Quicksort can then recursively sort the sub-arrays

The steps are:

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with
values less than the pivot come before the pivot, while all
elements with values greater than the pivot come after it
(equal values can go either way). After this partitioning,
the pivot is in its final position. This is called the
partition operation.
3. Recursively apply the above steps to the sub-array of
elements with smaller values and separately to the
sub-array of elements with greater values.
"""

import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

array = [random.randint(-5000, 2000) for _ in range(250000)]
start = time.time()
sorted_array = quicksort(array)
end = time.time()
print("Sorted array:", sorted_array)
print("Time taken:", end - start)