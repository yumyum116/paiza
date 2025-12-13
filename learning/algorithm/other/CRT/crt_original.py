#! /usr/bin/env python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def chinese_remainder_thorem(p1, p2, r1, r2):
    if gcd(p1, p2) != 1:
        return None
    for i in range(p2):
        x = p1 * i + r1
        if x % p2 == r2:
            return x
