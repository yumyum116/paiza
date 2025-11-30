#! /usr/bin/env python

"""
 # Approach
   Devide an array into two groups whose size is half of the original.
   Compare each element and insert a smaller element into the original array.
   Iterate until the element of each sub-array is INF.
"""

INF = 1000000001
count = 0

def merge(array, left, mid, right):
    global count
    
    larray = array[left:mid]
    rarray = array[mid:right]
    
    larray.append(INF)
    rarray.append(INF)
    
    lindex, rindex = 0, 0
    for i in range(left, right):
        if larray[lindex] < rarray[rindex]:
            array[i] = larray[lindex]
            lindex += 1
        else:
            array[i] = rarray[rindex]
            rindex += 1
            count += 1
    
def merge_sort(array, left, right):
    if left + 1 >= right:
        return
    
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid, right)
    merge(array, left, mid, right)
