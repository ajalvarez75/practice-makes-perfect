numbers_list = [1,2,3,4,5,6,7,8,9,10]

#regular
new_list = []

for numbers in numbers_list:
	new_list.append(numbers*numbers)

print(new_list)

#comprehension
new_list = [n*n for n in numbers_list]

print(new_list)