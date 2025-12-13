#include <string.h>

int	gcd(int a, int b)
{
	int	tmp;
	while (b)
		tmp = a;
		a = b;
		b = tmp % b;
	return (a);
}

int	chinese_remainder_thorem(p1, p2, r1, r2)
{
	if (gcd(p1, p2) != 1)
		return NULL;
	int	x;
	for (int i; p2; i++)
	{	x = p1 * i + r1;
		if (x % p2 == r2)
			return (x);
	}
}
