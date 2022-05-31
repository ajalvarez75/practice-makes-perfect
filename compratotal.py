#funcion donde le pase el total de una compra y que se aplique un descuento basado en los siguientes montos
#100 o menos no descuento
#100 y 500 5% de descuento
#500 y 100 10% de descuento
#mas de 1000 15% de descuento

def descuento(compra):
	porcentaje_descuento=[.0, .05, .10, .15]
	niveles=[100,500,1000]

	for i in porcentaje_descuento:
		compra_descuento=compra-(compra*i)
	

descuento(400)

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))


value=50
buy=10
value2=5
some=buy*2
print(some if buy>=value2 else buy)
    

compra=100
if compra>=0 and compra<=100:
	print(True)

a=5
b=3
c=a*b

if c==a*b:
	print("mm")
