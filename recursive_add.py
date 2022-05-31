def range(min,max):
	if min==max:
		return 0
	
	else:
		print(min)
		return range(min+1,max)

range(1,21)

