email=[1, "1", "@", 1.5, "alvar@"]

busquedad1=sum(1 for item in email if item==(1))
print(busquedad1)

busquedad2=sum(1 for item in email if item==("1"))
print(busquedad2)

busquedad3=sum(1 for item in email if item==("@"))
print(busquedad3)

busquedad4=sum(1 for item in email if item==(1.5))
print(busquedad4)

email2="Alvaro@ Alv@rez"

busquedad5=sum(1 for item in email2 if item==("@"))
print(busquedad5)