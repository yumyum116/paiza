#include <stdbool.h>
#include <math.h>
#include <stdio.h>

bool	is_prime(int n)
{
	if (n <= 1)
		return false;

	int limit = (int)sqrt(n);
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
