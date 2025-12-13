#! /usr/bin/env python

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

# extended euclidean algorithm
def modinv(a, m):
	x0, x1 = 1, 0
	b = m
	while b:
		q = a // b
		a, b = b, a % b
		x0, x1 = x1, x0 - q * x1

	return x0 % m

def	crt(p1, p2, r1, r2):
	if gcd(p1, p2) != 1:
		return None

	m1_inv = modinv(p1, p2)
	x = (r2 - r1) * m1_inv % p2

	return p1 * x + r1
