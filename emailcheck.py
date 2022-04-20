'''Crea un programa que evalúe si una dirección de correo electrónico es 
válida o no en función de si tiene “@” o “.” 
Hay que tener en cuenta que la dirección se considera correcta 
si solo tiene una “@” y si tiene uno o más “.”'''

email=input("Please enter your email: ")

at=sum(1 for item in email if item==("@"))
period=sum(1 for item in email if item==("."))

if at!=1 or period==0:
	print("correo incorrecto")
else:
	print("correo correcto")
