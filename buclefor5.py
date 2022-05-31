#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital 
#obtenido en la inversión cada año que dura la inversión.

inversion=int(input("Por favor introducir el valor a invertir: "))
interes_anual=int(input("interes anual: "))
años=int(input("plazo de la inversion: "))

for i in range(años):
	inversion+=(inversion*(interes_anual/100))
	
	print(str(i+1), "año" if i<1 else "años", "de inversion", inversion)
