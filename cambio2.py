def division(devuelta):
	cambios=[1000,500,200,100,50]
	minimo_valor=cambios[-1]
	if devuelta % minimo_valor >= 1:
		print("No es posible devolver menos de: ", minimo_valor)

	elif devuelta>=50:
		for cambios in cambios:
			division_veces=devuelta//cambios
			devuelta=devuelta-(cambios*division_veces)
			if division_veces>=1:
				print(cambios, division_veces) 

division(12350)



