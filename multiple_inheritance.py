class class1:
	pass

class class2:
	pass

class class3:
	pass

class class4(class1,class2,class3):
	pass

print(class4.mro())