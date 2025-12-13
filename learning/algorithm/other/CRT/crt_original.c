#include <stdio.h>

int	gcd(int a, int b)
{
	int	tmp;
	while (b)
	{
		tmp = a;
		a = b;
		b = tmp % b;
	}
	return (a);
}

int	chinese_remainder_thorem(int p1, int p2, int r1, int r2)
{
	if (gcd(p1, p2) != 1)
		return -1;
	int	x;
	int	rr2 = ((r2 % p2) + p2) % p2;
	for (int i = 0; i < p2; i++)
	{
		x = p1 * i + r1;
		if ((x % p2 + p2) % p2 == rr2)
			return (x);
	}
	return (-1);
}

int	main(void)
{
	int p1, p2, r1, r2;
	p1 = 31;
	p2 = 53;
	r1 = 3;
	r2 = 5;

	int res = chinese_remainder_thorem(p1, p2, r1, r2);
	printf("%d\n", res);
}
