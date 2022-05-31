def understanding_kwargs(a, b, *args, **kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)

understanding_kwargs(1,2,3,4,5,"a",obj1=2,z=10)