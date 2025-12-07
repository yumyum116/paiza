#include <stdbool.h>
#include <stdio.h>

double	my_sqrt(double n)
{
	double	x = n;

	for (int i = 0; i < 20; i++)
		x = 0.5 * (x + n / x);

	return x;
}

bool	is_prime(int n)
{
	if (n <= 1)
		return false;

	double x = (double)n;

	int limit = (int)my_sqrt(x);
	for (int i = 2; i <= limit; i++)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}

int	main(void)
{
	printf("%s\n", is_prime(999999937) ? "true" : "false");
}
