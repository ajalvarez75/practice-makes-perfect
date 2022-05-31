#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def multiplicacion(a,b):
	print("tablas de multiplicar: ")
	for i in range(1,a+1):
		for j in range(1,b+1):
			print(j,"x",i," =" if i<10 else "=",(i*j), end="\t")
		print()

multiplicacion(10,10)


