#hacer todas las combinaciones de 2 numeros de 2 digitos.

import itertools

def combinaciones(numeros):
	lista=list(range(numeros))
	result=itertools.combinations(lista,2)
	a,b=0,0

	for a in result:
		values = ''.join(map(str, a))
		a=b
		b+=1
		x="0"
		y="0"
		z="0"
		if a<=8:
			print(x+y+""+values,)

		if a>8 and a<=98:
			print(x+values,)

		if a>98 and int(values)>10 and int(values)<100:
			print(x+values+""+x,)

		if a>100 and len(values)==3:
			print(x+values,)

		if a>100 and len(values)==4:
			print(values,)

combinaciones(100)