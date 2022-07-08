x="sdfasdfasñlkjsdalfs?sdfsjnd1231468asdfjbasd1a"
counter=0

for i in x:
	try:
		i==int(i)
		counter+=1
	except ValueError:
		pass

print(counter)