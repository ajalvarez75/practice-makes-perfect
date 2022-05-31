def insertando(cosa):
	algo=[]
	limite=cosa-1

	for cosa in range(1,cosa+1):
		algo.append(cosa)
		if cosa<limite and cosa%5==0:
			algo.append("a")
	return(algo) 

print(insertando(10))
print()