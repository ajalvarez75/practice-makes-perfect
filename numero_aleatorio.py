#funcion que genere numeros aleatorios y me diga si el numero es positivo, negativo o cero

from random import gauss
import random


def aleatoria(numero):
	for i in range(numero):
		number = random.randint(-10,10)
		if number>=1:
			print(int(number), "is positive")
		elif number<=-1:
			print(int(number), "is negative")
		else:
			print(int(number), "is zero")

aleatoria(10)
