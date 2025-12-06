#! /usr/lib/env python

def is_prime_sqrt(n):
	if n <= 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

print(is_prime_sqrt(999999937))
