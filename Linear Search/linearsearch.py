arr = [52,-54,10,23,25,56,87]
given = 10

def linearsearch(arr,given):
    if len(arr) == 0:
        print('Empty Array')

    for i in range(len(arr)):
        check = arr[i]
        if check == given:
            return f'Item found at {i} index'
    return 'Item not found'

def min(arr):
    ans = arr[0]
    for i in range(len(arr)):
        if arr[i]<ans:
            ans = arr[i]
    return ans

#print(linearsearch(arr, given))
print(min(arr))