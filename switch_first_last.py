numeros = "12345"
lista_numeros = list(numeros)

def intercambio(lista_numeros):
	last=len(lista_numeros)+1
	lista_numeros.insert(0, lista_numeros.pop(-1))
	lista_numeros.insert(last, lista_numeros.pop(1))
	return lista_numeros

print(intercambio(lista_numeros))