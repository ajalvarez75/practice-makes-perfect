def combinacion_doble(num1, num2):
    lista=[]
    a,b=0,1
    for i in range(0,num1,1):
        for j in range(0,num2,1):
            for x in range(0,num1,1):
                for y in range(0,num2,1):
                    i=str(i)
                    j=str(j)
                    x=str(x)
                    y=str(y)
                    z=i+j+x+y
                    invertida=z[::-1]
                    lista.append(invertida)             

                    if i=="0" and j=="0" and x=="0" and y=="0":
                        continue

                    if i==x and j==y:
                         continue
                       
                    if z in lista:
                        continue
                    print(z, end=", ")

combinacion_doble(10,10)