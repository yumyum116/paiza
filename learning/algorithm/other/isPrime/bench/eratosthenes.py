#! /usr/bin/env python

MAX_A = 6000000

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime

n = int(input())
arr = [int(input()) for _ in range(n)]

is_prime_table = eratosthenes(MAX_A)

out = []
for x in arr:
    out.append("pass" if is_prime_table[x] else "failure")

print("\n".join(out))
