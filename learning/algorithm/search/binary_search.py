#! /usr/bin/env python

def binary_search(array, length, n, k):
    array.sort()

    left = 0
    right = length

    while right - left > 1:
        mid = (left + right) // 2

        if can_divide(mid, array, length, n, k):
            right = mid
        else:
            left = mid

    return right

def can_divide(max_len, array, length, n, k):
    previuos = 0
    current = 0
    pieces = 1


    for i in range(k):
        segment = array[i] - previuos

        if segment > max_len:
            return False

        if current + segment <= max_len:
            current += segment
        else:
            pieces += 1
            current = segment

        previuos = array[i]

    segment = length - previuos
    if segment > max_len:
        return False

    if current + segment > max_len:
        pieces += 1

    return pieces <= n

print(binary_search([1, 3, 8], 10, 3, 3))
