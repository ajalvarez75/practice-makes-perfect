def addition(*args):
	result = 0
	for i in args:
		result += i
	return result

print(addition())

print(addition(1,5))

print(addition(1,10,9))