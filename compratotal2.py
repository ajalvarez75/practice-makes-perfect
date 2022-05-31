def compra_descuento(compra):

	if compra>=0 and compra<=100:
		total_descuento=compra-(compra*0)

	elif compra>=101 and compra<=500:
		total_descuento=compra-(compra*.05)

	elif compra>=501 and compra<=1000:
		total_descuento=compra-(compra*.10)

	elif compra >= 1001:
		total_descuento=compra-(compra*.15)
	
	print("total sin descuento:" if total_descuento==compra-(compra*0) else "total con descuento:",
		total_descuento)

compra_descuento(95)
