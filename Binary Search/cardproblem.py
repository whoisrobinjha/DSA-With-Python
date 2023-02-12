arr = [13,11,12,7,4,1,0]
target = 7

def findCard(arr, target):  
    start = 0
    end = len(arr)
    while(start < end):
        mid = start + (end - start) //2
        if(arr[mid] < target):
            end = mid - 1
        elif(arr[mid] > target):
            start = mid + 1
        else:
            return mid
    return -1

print(findCard(arr, target))
