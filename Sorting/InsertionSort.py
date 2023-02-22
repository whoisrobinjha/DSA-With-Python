"""Insertion sort is a simple sorting algorithm that builds
the final sorted array (or list) one item at a time.
It is much less efficient on large lists than more
advanced algorithms such as quicksort, heapsort, or merge
sort."""

"""
1. The insertion_sort function takes an array arr as input.
2. The length of the array is stored in the variable n.
3. We loop over the array starting from the second element (index 1) to the end.
4. For each element, we store it in the variable key.
5. We compare the key to the elements before it in the array, starting from the previous element (index i-1).
6. If an element is greater than the key, we shift it to the right by one position.
7. We continue this process until we find an element that is less than or equal to the key.
8. We insert the key into its correct position in the array.
9. We repeat this process for all elements in the array.
10. Finally, we return the sorted array.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [5,4,3,2,1]
print(insertion_sort(arr))