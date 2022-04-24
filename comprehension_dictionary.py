#comprehension
lista=[valor for valor in range(0, 101) if valor % 2 == 0]

dictionary = { indice:valor for indice, valor in enumerate(lista)}

print(dictionary)