'''def re_factorial(n):
	if n==0:
		return 1

	else:
		n = n * re_factorial(n - 1)
		return n

print(re_factorial(5))'''

def re_factorial(n):
	if n==0:
		return 1

	else:
		return n * re_factorial(n-1)

print(re_factorial(5))