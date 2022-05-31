#una funcion q reciba de cambio y la funcion va decir el minimo # de monedas que puede devolver
#las monedas son 50, 100, 200, 500, 1000

#eje: cambio = 1850
#resta es 5 por que seria una 1000., una 500 y una de 200 y una 50. y una de 100

#eje: cambio = 500
#respuesta = 1 

#eje cambio = 750
#respuesta = 3

#lo que recibe la funcion: un valor a devolver
#lo que va retornaar: la cantidad de monedas minimas para cubrir el valor a devolver
#establecer una variable para valor de moneda
#suma de valores mas grandes que igualen a el cambio.

def cambio(valor_cambio):

	a, veces1, restante1 = 1000, 0, 0
	b, veces2, restante2 = 500, 0, 0
	c, veces3, restante3 = 200, 0, 0
	d, veces4, restante4 = 100, 0, 0
	e, veces5, restante5 = 50, 0, 0

	if valor_cambio>=a:
		veces1=(valor_cambio//a)
		restante1=valor_cambio-(a*veces1)
		
	elif valor_cambio<a:
		restante1=valor_cambio

	if restante1>=b:
		veces2=(restante1//b)
		restante2=restante1-(b*veces2)
		
	elif restante1<b:
		restante2=restante1

	if restante2>=c:
		veces3=(restante2//c)
		restante3=restante2-(c*veces3)
		
	elif restante2<c:
		restante3=restante2

	if restante3>=d:
		veces4=(restante3//d)
		restante4=restante3-(d*veces4)
		
	elif restante3<d:
		restante4=restante3

	if restante4>=e:
		veces5=(restante4//e)
		restante5=restante4-(e*veces5)
		
	elif valor_cambio<e:
		print("Atencion! se le devolvera la cantidad de: ",restante3-restante4,
			"\nya que no podemos devolver montos inferiores a: ", e)

	if valor_cambio>=e:
		print("Minimo total de monedas para cambio: ", veces1+veces2+veces3+veces4+veces5)


cambio(300)


