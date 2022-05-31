def understanding_kwargs(a, b, Option=True, **kwargs):
	print(f'this is the result from a and b: ', a, "y", b)
	print(Option)
	print(kwargs)

understanding_kwargs(1,2,obj1=5,obj2=6)