#! /usr/bin/env python

def gcd_two(a, b):
    if a == 0:
        return 0
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(*numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd_two(result, numbers[i])
    return result

n = int(input())
nums = [int(input()) for _ in range(n)]

print(gcd_multiple(*nums))
