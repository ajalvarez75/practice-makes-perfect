lista = []

for valor in range(0, 101):
	lista.append(valor)

print(lista)

lista=[valor for valor in range(0, 101) if valor % 2 == 0]

print(lista)