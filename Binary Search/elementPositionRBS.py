#python program to find the position of an element in a rotated array using binary search

def find_element_in_rotated_array(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) >> 1
        if arr[mid] == target:
            return mid
        if arr[start] <= arr[mid]:
            if arr[start] <= target and target <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target and target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return 0

arr = [5,6,7,1,2,3,4]
target = 6
print(find_element_in_rotated_array(arr, target))