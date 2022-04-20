'''Crea un programa que pida números positivos indefinidamente. 
El programa termina cuando se introduce un número negativo. 
Finalmente el programa muestras la suma de todos los números introducidos.'''

number= int(input("please, enter a positive number: "))
plus=0

while number>0:
	plus=plus+number
	number= int(input("Please, enter another number: "))

print("the total sum from entered numbers is: ", str(plus))