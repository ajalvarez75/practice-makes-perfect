def diagonal(n):
	for i in range(1,n+1,1):
		print(" "*i,"$" if n==1 else "\\", end="\n")

diagonal(5)