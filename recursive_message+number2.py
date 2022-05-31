def mensaje(min,max,mensajes):
	if min==max:
		print(mensajes)

	else:
		print(mensajes)
		return mensaje(min+1,max,mensajes)

mensaje(1,2,"alvaro")