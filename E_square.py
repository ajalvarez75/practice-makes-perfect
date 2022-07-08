def square(n):
	for i in range(1,n+1,1):
		for j in range(1,n+1,1):
			if j>n-1:
				print("#"*j)
square(5)