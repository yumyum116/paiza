#! /usr/bin/env python

import sys

def eratosthenes_odd(n):
    if n < 2:
        return []

    size = (n + 1) // 2
    is_prime = [True] * size
    is_prime[0] = False  # 1 は非素数

    limit = int(n ** 0.5) // 2
    for i in range(1, limit + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            for j in range(start, size, p):
                is_prime[j] = False

    return is_prime

if __name__ == "__main__":
    n = int(sys.argv[1])
    eratosthenes_odd(n)
