numeros = "12345"
lista_numeros = list(numeros)

lista_numeros[0], lista_numeros[-1] = lista_numeros[-1], lista_numeros[0]

print(lista_numeros)