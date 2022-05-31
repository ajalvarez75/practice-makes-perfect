#functions are objects:

def Alvaro(text):
	return text.upper()

print(Alvaro('Javier'))

saludo = Alvaro

print(saludo('Alvaro'))
print()

#Function like argument to other function:

def text(text):
	return text.upper()

def title(text):
	return text.lower()

def book(func):
	reading = func('what?')
	print(reading)

book(text)
book(title)
print()

#return a function from other function.

def number1(x):
	def number2(y):
		return x+y

	return number2

add = number1(7)

print (add(10)) 



