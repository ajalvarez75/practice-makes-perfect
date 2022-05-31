#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


contraseña="alvaro"
almacenamiento=input("por favor introduzca la contraseña: ")

while contraseña!=almacenamiento:
	almacenamiento=input("por favor introduzca la contraseña: ")
print("contraseña correcta!")


