#funcion me va indicar cual es el ultimo digito de un numero, si es mayor que 5 o menor que 6 y no cero o cero

import random

def last_digit(n):

	for i in range(n):
		random_number=random.randint(-1000,1000)
		last=abs(random_number)%10

		if random_number>5 and last!=0 and last>5:
			print(random_number, last, "and is greater than 5")

		elif last==0:
			print(random_number, last, "and is 0")

		elif last!=0 and last<6 or random_number<0:
			print(random_number, -last if random_number<0 else last, "and is less than 6 and not 0")

last_digit(10)