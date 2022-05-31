def range(number):
	if number==0:
		print()

	elif number>=1:
		print(number)
		return range(number-1)

range(2)