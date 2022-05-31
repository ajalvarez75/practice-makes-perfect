class Componentes:
	def __init__(self, motor, llantas, capacidad_tanque):

		self.motor = motor
		self.llantas = llantas
		self.capacidad_tanque = capacidad_tanque

	def Modelo(self):
		print ("Motor: ", self.motor, "\nLLantas: ", self.llantas, "\nCapacidad_tanque: ", self.capacidad_tanque)

class Pintura:
	color = "Color: negro"

class Producto(Componentes, Pintura):
	def Prototipo(self):
		print("las caracteristicas de la moto son: ", "\nCilindraje: ", self.motor, "\nLLantas: ", self.llantas, 
			"\nCapacidad_tanque: ", self.capacidad_tanque,)
		print(self.color)


moto1 = Producto('50cc','off road 70/30', '15litros')

moto1.Prototipo()

print(Producto.mro())

		