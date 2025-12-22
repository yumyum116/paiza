#! /usr/bin/env python

import sys

def eratosthenes_fast(n):
    if n < 2:
        return []

    size = (n + 1) // 2
    is_prime = bytearray(b"\x01") * size
    is_prime[0] = 0

    limit = int(n ** 0.5) // 2
    for i in range(1, limit + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            is_prime[start::p] = b"\x00" * (((size - start - 1) // p) + 1)

    return is_prime

if __name__ == "__main__":
    n = int(sys.argv[1])
    eratosthenes_fast(n)
