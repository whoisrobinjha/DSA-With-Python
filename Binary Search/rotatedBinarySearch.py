#Rotated Binary Search Implementation

def rotated_binary_search(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) >> 1
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid
        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

arr = [16,1,3,5,6,7,8,9,11,15]
print(rotated_binary_search(arr))