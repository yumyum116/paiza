#! /usr/bin/env python

"""
 # Approach
   Select a pivot element to partition the array.
   Traverse the array and swap elements so that all values smaller than the pivot
   are placed on its left side, and larger values on its right side.
   Then recirsively apply the same process to each partition until the array becomes sorted.
"""

def quick_sort(array, left, right):
    if left + 1 >= right:
        return 

    pivot = array[right - 1]
    
    current_index = left
    for i in range(left, right - 1):
        if array[i] < pivot:
            array[current_index], array[i] = array[i], array[current_index]
            current_index += 1
            count += 1
    
    array[right - 1], array[current_index] = array[current_index], pivot

    quick_sort(array, left, current_index)
    quick_sort(array, current_index + 1, right)
