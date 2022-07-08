#hacer todas las combinaciones de 3 digitos comenzando con 012

import itertools

def combinaciones(numeros):
	lista=list(range(numeros))
	result=itertools.combinations(lista,3)

	for a in result:
		#print("".join(map(str,a)), end=",")
		print(*a, sep="",)

combinaciones(10)