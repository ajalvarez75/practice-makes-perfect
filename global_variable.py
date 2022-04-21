#function using a global variable.
x = "Alvaro"

def function():

	print("my name is: " + x)

function()


#function in this case use the local variable instead the global.
x = "Alvarez"

def function():

	x = "Javier"

	print("my name is: " + x)

function()

print("my name is: " + x)


#with the instrution global the interpreter will consider our local
#function as global even if we had declared a previous global variable. 
x = "Cardenas"

def function():
	global x
	x = "Javier"

	print("my name is: " + x)

function()

print("my name is: " + x)