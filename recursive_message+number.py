#the function should recieve a message and number, then, it it should print the message.

def mensaje(veces, mensajes):
	if veces<=0:
		return

	else:
		print(mensajes)
		return mensaje(veces-1,mensajes)

mensaje(1,"alvaro")

