#! /usr/lib/env python

def is_prime_even(n):
	if n <= 1:
		return False

	if n == 2:
		return True

	for i in range(3, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
		i += 2

	return True

print(is_prime_even(999999937))
