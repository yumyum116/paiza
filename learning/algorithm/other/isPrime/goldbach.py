#! /usr/bin/env python

def goldbach_conjecture(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for p in range(n // 2, 1, -1):
        q = n - p
        if is_prime[p] and is_prime[q]:
            return p, q
