#! /usr/bin/env python

"""
 Constraints:
    A series of gaps, denoted by 'gap', is given as 'gap_sequence'.
"""

def insertion_sort(array, n, gap):
    for i in range(gap, n):
        x = array[i]
        
        j = i - gap
        while j >= 0 and array[j] > x:
            array[j + gap] = array[j]
            j -= gap
        
        array[j + gap] = x

def shell_sort(array, n, gap_sequence):
    for gap in gap_sequence:
        insertion_sort(array, n, gap)
