#escribir todas las combinaciones posibles de dos digitos
import itertools

def combinaciones(numeros):
	lista=list(range(numeros))
	result=itertools.combinations(lista,2)

	for a in result:
		#print("".join(map(str,a)), end=",")
		print(*a, sep="",)

combinaciones(10)