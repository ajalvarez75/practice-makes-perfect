
n=10
x=[1,2,"b","b","b"]
index=0
for i in range(1, n+1, 2):

    for j in x:
        index+=1   
        print(j,"casa " if index %5!=0 else "", end="")
    print("")
