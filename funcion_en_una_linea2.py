numeros = "12345"
lista_numeros = list(numeros)

def intercambio(lista_numeros):
	lista_numeros[0], lista_numeros[-1] = lista_numeros[-1], lista_numeros[0]

intercambio(lista_numeros)
print(lista_numeros)