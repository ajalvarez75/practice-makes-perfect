#regular

my_list = []

for value in range(0, 101):
	my_list.append(value)

print(my_list)


#comprehension
my_list = [value for value in range(0, 101) if value % 2 == 0]

print(my_list)