def biggest(num1,num2,num3):
	if num1 > num2 and num1 > num3:
		print(num1)
	elif num2 > num1 and num2 > num3:
		print(num2)
	elif num3 > num1 and num3 > num2:
		print(num3)	
	else:
		print("the numbers are equal")

biggest(6,5,4)