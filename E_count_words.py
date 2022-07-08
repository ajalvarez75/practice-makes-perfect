x=" this is an   excersice to count the    words  "
counter=0
dictx=[]

for i in x:
	if i==" " and dictx==[]:
		continue

	if i==" " and dictx[-1]==" ":
		continue
	else:
		dictx.append(i)

if dictx[-1]==" ":
	dictx.pop(-1)

newx="".join(dictx)
words=newx.count(" ")
print(newx)
print(words+1)





