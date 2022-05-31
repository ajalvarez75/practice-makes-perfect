from datetime import date

def edad(año, mes, dia):

	fecha_nacimiento = date(año, mes, dia)
	today=date.today()

	edad_actual1 = today-fecha_nacimiento
	edad_actual2 = edad_actual1.days/365
	meses = (edad_actual2*12)-(int(edad_actual2)*12)
	dias = (meses-int(meses))*(365/12)
	dias2 = meses

	print(int(edad_actual2),"años -", int(meses), "meses -", int(dias), " dias", dias2) 

edad(1990,5,22)