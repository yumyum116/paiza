#! /usr/bin/env python

import sys

def eratosthenes_bytearray(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0

    return is_prime

if __name__ == "__main__":
    n = int(sys.argv[1])
    eratosthenes_bytearray(n)
