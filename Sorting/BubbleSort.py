"""Bubble sort, sometimes referred to as sinking sort, is a
simple sorting algorithm that repeatedly steps through
the list to be sorted, compares each pair of adjacent
items and swaps them if they are in the wrong order
(ascending or descending arrangement). The pass through
the list is repeated until no swaps are needed, which
indicates that the list is sorted."""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr

arr = [56,12,8,56,-9,0,564]
print(bubble_sort(arr))