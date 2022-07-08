x="understood"
y="understand"
distance=0

if len(x)!=len(y):
	print("the word must have the same length")

for i in range(len(x)):
	if x[i]!=y[i]:
		distance+=1
print(distance)

