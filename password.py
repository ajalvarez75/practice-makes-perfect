'''Crea un programa que pida por teclado introducir una contraseña. 
La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. 
Si la contraseña es correcta, el programa imprime “Contraseña OK”. 
En caso contrario imprime “Contraseña errónea”'''


password=input("Please, enter your new password: ")
'''carateres=' '
minimocarateres=len(password)'''

if (' ' in password)==True or len(password)<8:
	print('wrong password')

else:
	print('password ok!')

