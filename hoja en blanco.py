from datetime import *
from random import *

tday=date.today()
print(tday.day)
print(tday.month)
print(tday.year)
print(tday)
print()

lista=["alvaro", "javier", 1.5]
x=" ".join(map(str, lista))
print(x)

def variable():
    global z
    z=1
variable()

print(z)