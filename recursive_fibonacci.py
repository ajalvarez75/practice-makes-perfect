# 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9

def re_fibonacci(n):
	if n <= 1:
		return n
	else:
		return re_fibonacci(n-1) + re_fibonacci(n-2)

print(re_fibonacci(4))

#interpretacion
#re_fibonacci(5) = re_fibonacci(4) + re_fibonacci(3)
#re_fibonacci(4) = re_fibonacci(3) + re_fibonacci(2)
#re_fibonacci(3) = re_fibonacci(2) + re_fibonacci(1)
#re_fibonacci(2) = re_fibonacci(1) + re_fibonacci(0)