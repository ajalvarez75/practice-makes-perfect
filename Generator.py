def generator():
	n=1
	yield n

	n+=1
	yield n

	n+=1
	yield n

for i in generator():
	print(i)