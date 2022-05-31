#Escribir un programa que pida al usuario un número entero y muestre por pantalla 
#un triángulo rectángulo como el de más abajo, de altura el número introducido.

niveles=int(input("ingrese el numero de niveles para el triangulo: "))

for i in range(niveles+1):
	print("*"*i)