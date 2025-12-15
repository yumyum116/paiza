#! /usr/bin/env python

@profile
def goldbach_conjecture(n):
    prime = [2]
    for i in range(3, n + 1, 2):
        for j in range(3, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    prime_combi = []
    for i in range(len(prime)):
        if n - prime[i] in prime:
            prime_combi.append([prime[i], n - prime[i]])
    if not prime_combi:
            return None

    max_res = -1
    max_idx = 0
    for j in range(len(prime_combi)):
        prod = prime_combi[j][0] * prime_combi[j][1]
        if prod > max_res:
            max_res = prod
            max_idx = j

    return prime_combi[max_idx]

n = 34240
result = goldbach_conjecture(n)
if result is None:
	print("No combination found")
else:
	for p in result:
		print(p)
