#adivinar numero, el juego va a generar un numero aleatorio entre 1 y 100,
#cuando el usuario ingresa el numero el programa le dice si necesita ingresar un numero mayor o menor
#hasta que logre adivinar el numero
import random

#def run():
numero_aleatorio = random.randint(1, 100)
numero_elegido = int(input("Elije un numero del 1 al 100 :"))
while numero_elegido != numero_aleatorio:
	if numero_elegido < numero_aleatorio:
        print("Busca un numero mas grande ")
    else:
        print("Busca un numero mas pequeño ")
    numero_elegido = int(input("Elije otro numero  :"))
print("Ganaste!")

#if __name__ == "__main__":
    #run()

