#Rotated Binary Search Implementation

def rotated_binary_search(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) >> 1
        if arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid + 1]:
            end = mid - 1
        else:
            start = mid + 1
    return mid 

arr = [6,7,8,9,11,15,19,1,3,5]
print(rotated_binary_search(arr))