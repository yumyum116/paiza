#! /usr/bin/env python

"""
 Constraints:
    A series of gaps, denoted by 'gap', is chosen by the algorithm.
"""

cnt = 0

def insertion_sort(array, n, gap):
    global cnt
    for i in range(gap, n):
        x = array[i]
        j = i - gap
        while j >= 0 and array[j] > x:
            array[j + gap] = array[j]
            j -= gap
            cnt += 1
            
        array[j + gap] = x
        
def shell_sort(array, n):
    gap_sequence = []
    
    tmp = n // 2
    while tmp > 0:
        gap_sequence.append(tmp)
        tmp //= 2
    if not gap_sequence:
        gap_sequence.append(1)
    
    m = len(gap_sequence)
    for i in range(m):
        insertion_sort(array, n, gap_sequence[i])
    
    return m, gap_sequence
