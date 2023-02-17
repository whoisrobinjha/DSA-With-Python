"""Cycle sort is an in-place, unstable sorting algorithm,
a comparison sort that is theoretically optimal in terms 
of the total number of writes to the original array, 
unlike any other in-place sorting algorithm. It is based 
on the idea that the permutation to be sorted can be 
factored into cycles, which can individually be rotated 
to give a sorted result."""

def cycle_sort(arr):
    n = len(arr)
    
    for cycle_start in range(0, n-1):
        item = arr[cycle_start]
        pos = cycle_start
        
        for i in range(cycle_start+1, n):
            if arr[i] < item:
                pos += 1
        
        if pos == cycle_start:
            continue
        
        while item == arr[pos]:
            pos += 1
        
        arr[pos], item = item, arr[pos]
        
        while pos != cycle_start:
            pos = cycle_start
            
            for i in range(cycle_start+1, n):
                if arr[i] < item:
                    pos += 1
            
            while item == arr[pos]:
                pos += 1
            
            arr[pos], item = item, arr[pos]
            
    return arr

arr = [10,9,8,7,6,5,4,3,1,0,-1,-2,-3]
print(cycle_sort(arr))