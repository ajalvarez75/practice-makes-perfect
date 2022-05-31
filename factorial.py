# *factorial de un numero y que retorne cual es.
# lo que recibe la funcion: un numero al cual se le va sacar su factorial
# lo que retorna mi funcion: la multuplicacion final del factorial.
# Por ejemplo, 5! = 5.4.3.2.1 = 120
# comienzo con el numero mayor
# termino en el numero 1
# se deben multiplicar los dos ultimos numeros
# tener en cuenta que el factorial de cero es 1

'''def factorial(n):

	a = n
	b = n-1
	
	for i in range(n,0,-1):

		#x = a*b
		#a = x
		#b = 
		a = list(i)

		return a

print(factorial(5))'''


'''n=5
for i in range(n,0,-1):
    print(i)'''

'''lista = [1*2*3*4*5]
lista2 = [5*4*3*2*1]

print(lista)
print(lista2)'''


'''lista=[1,'*',2,'*',3]
nueva_lista=''.join([str (item) for item in lista])
nuevo=nueva_lista*1
print(nuevo)'''

'''n=20
my_list = [*range(n,0,-1)]
print(my_list)'''

'''def factorial(my_list):

	if my_list == 0:
		my_list=1

	else:
		my_list = [*range(my_list,0,-1)]
		for factorial in range(0,len(my_list)):
			my_list.insert(factorial*2,'*')

		my_list.pop(0)
		the_factorial=''.join(my_list)

	return the_factorial

print(factorial(5))'''

def factorial(my_list):

	if my_list == 0:
		return  1

	else:
		result=1
		my_list = [*range(my_list,0,-1)]
		for i in my_list:
			result = result*i

	return result

print(factorial(5))

'''def factorial(my_list):

	if my_list != 0:
		result=1
		my_list = [*range(my_list,0,-1)]
		for i in my_list:
			result = result*i
		return result

	elif my_list==0:
		return 1

print(factorial(0))'''
