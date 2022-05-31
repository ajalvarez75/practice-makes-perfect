#*funcion de fibonachi y pedirle el valor en la posicion deseada.

#lo que recibe la fucion: input con la posicion de un valor de la serie de fibonacci
#que retorna mi funcion: el valor correspondiente al input
#serie de fibonacci: 1 1 2 3 5 8 13 21 34...
#comienzo a contar desde el primer numero de la serie(1)
#establecer el segundo numero de la serie
#generar el siguiente numero basado en los dos ultimos valores
#detenerme cuando haya generado el numero de elementos y devolver el valor

def fibonacci(n):
	
	a = 1
	b = 1
	c = 1

	for i in range(n-2):
		c = b+a
		a = b
		b = c

	return c

print(fibonacci(3))