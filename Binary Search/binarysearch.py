arr = [1,3,6,12,45,89] 
target = 13 

def BinarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    mid = 0
    
    if arr[0] < arr[-1]:
        while start <= end:
            mid = start + (end - start)//2
            if target < arr[mid]:
                end = mid-1     
            elif target > arr[mid]:
                start = mid+1
            else:
                return mid
        return -1
    
    else:
        while start <= end:
            mid = start + (end - start)//2
            if target < arr[mid]:
                start = mid + 1            
            elif target > arr[mid]:
                end = mid - 1
            else:
                return mid
        return -1


def binarySearch(arr, target):
    start = 0
    end = len(arr)

    while(start < end):
        mid = int(start + (end - start) / 2)
        if(arr[mid] < target):
            start = mid + 1
        elif(arr[mid] > target):
            end = mid - 1
        else:
            return mid
    
    return -1

def returnCieling(arr, target):
    start = 0
    end = len(arr)

    while(start < end):
        mid = int(start + (end - start)/2)
        if(arr[mid] < target):
            start = mid + 1
        elif(arr[mid] > target):
            end = mid - 1
        else:
            return mid
    return arr[start]

def returnFloor(arr, target):
    start = 0
    end = len(arr)

    while(start < end):
        mid = int(start + (end - start)/2)
        if(arr[mid] < target):
            start = mid + 1
        elif(arr[mid] > target):
            end = mid - 1
        else:
            return arr[mid]
    return arr[end]

print(returnFloor(arr, target))
