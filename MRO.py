# MRO = Method Resolution Order.

class A ():
	"""docstring for ClassName"""
	pass

class B (A):
	pass

class C (A):
	pass

class D(B, C):
	pass

print(D.mro())
print(D.__mro__)
	
