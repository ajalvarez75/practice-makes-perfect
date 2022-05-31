#find and count a letter inside a string

'''def find_count(text, find):
	x = sum(1 for letter in text if letter==(find))
	return x

print(find_count("alvaro", "a"))'''

def find_X(text, find):
	x=text.count(find)
	return x

print(find_X("alvaro javier", "r"))