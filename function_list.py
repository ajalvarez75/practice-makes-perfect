#incorrect
def add9(my_list=[]):
	my_list.append(9)
	print(my_list)

add9()
add9()
add9()

#correct
def add8(a=None):
	if a==None:
		a=[]
	a.append (8)
	print(a)

add8()

add8()