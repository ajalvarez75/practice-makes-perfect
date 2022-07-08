def multiplication(num1,num2):
	for i in range(num1):
		for j in range(num2):
			print(f'{i*j:02}',"," if j<9 else"$", end="\t", sep="")
		print()
multiplication(10,10)