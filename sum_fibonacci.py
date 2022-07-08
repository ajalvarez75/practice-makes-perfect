#  a b c
#  1 1 2 3 5  8  13 21
#  1 2 3 4 5  6  7  8
#          12 20 33 54

def sum_fibonacci(ultimo):
	a,b,c=0,1,1
	z=0
	while ultimo>c:
		c=a+b
		a=b
		b=c
		z+=c
	if ultimo!=c:
		print((z+1)-c)
	elif ultimo==c:
		print(z+1)	
			
sum_fibonacci(20)