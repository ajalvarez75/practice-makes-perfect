#escribir todas las combinaciones posibles de dos digitos
import itertools

def combinaciones(numeros):
	lista=[]

	for i in range(numeros):
		lista.append(i)

	result=itertools.combinations(lista,2)

	for a in result:
		#print("".join(map(str,a)), end=",")
		print(*a, sep="", end=", ")

combinaciones(10)