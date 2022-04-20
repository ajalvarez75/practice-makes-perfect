'''Crea un programa que pida números infinitamente. 
Los números introducidos deben ser cada vez mayores 
El programa finalizará cuando se introduce un número menor que el anterior.'''


number1=int(input("please enter a number: "))
number2=int(input("please enter a bigger number than "+ str(number1) +": "))

while number2>number1:
	number1=number2
	number2=int(input("please enter a bigger number than "+ str(number1) +": "))

print()
#help me to generate an space between the enter data and the last print.
print(number2, "is not bigger than", str(number1))
