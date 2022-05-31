#creacion de decorador
def Function_A(Function_B):
	def Function_C():
		print('Before the decoration function')

		Function_B()
		print('After the decoration function')

	return Function_C

#funcion a ser decorada
@Function_A
def Hello():
	print('Hola mundo!!')

Hello()