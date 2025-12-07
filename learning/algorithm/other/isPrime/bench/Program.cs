// See https://aka.ms/new-console-template for more information

bool	IsPrime(int n)
{
	if (n <= 1)
		return false;

	int limit = (int)Math.Sqrt(n);

	for (int i = 2; i <= limit; i++)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}

Console.WriteLine(IsPrime(999999937));
