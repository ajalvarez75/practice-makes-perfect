#ab c
# 1 1 2 3 5 8 13
# 1 2 3 4 5 6 7

def fibonacci(numero):
	a,b=0,1

	print (1)
	
	for i in range(numero-1):
		c=a+b
		a=b
		b=c
		print(c)

fibonacci(3)