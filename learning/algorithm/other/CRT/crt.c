#include <stdio.h>

int	gcd(int a, int b)
{
	int tmp;
	while (b)
	{
		tmp = a;
		a = b;
		b = tmp % b;
	}
	return (a);
}

int	modinv(int a, int m)
{
	int x0 = 1, x1 = 0;
	int	b = m;
	int	tmp_a, tmp_x0;
	while (b)
	{
		int	q = (int) a / b;
		tmp_a = a, tmp_x0 = x0;
		a = b;
		b = tmp_a % b;
		x0 = x1;
		x1 = tmp_x0 - q * x1;
	}
	return (int)(x0 % m);
}

int	crt(int p1, int p2, int r1, int r2)
{
	if (gcd(p1, p2) != 1)
		return (-1);
	int	m1_inv = modinv(p1, p2);
	int	x = (r2 - r1) * m1_inv % p2;

	return (p1 * x + r1);
}

int	main(void)
{
	int p1, p2, r1, r2;
	p1 = 31;
	p2 = 53;
	r1 = 3;
	r2 = 5;

	int res = crt(p1, p2, r1, r2);
	printf("%d\n", res);
}
