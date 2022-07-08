def sum_modulus(number):
	a=0
	for i in range(1,number+1):
		if i%3==0 or i%5==0:
			a+=i
	print(a)

sum_modulus(9)