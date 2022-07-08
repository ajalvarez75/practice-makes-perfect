from random import *
#randint
n=3
for i in range(1,n+1):
    i=randint(1,100)
    print(i)
print()

#randrange
a=randrange(100)
print(a)
print()

b=randrange(1,11)
print(b)
print()

c=randrange(0,101,10)
print(c)
print()

persons=["Alvaro", "Javier", "Veronica", "Martha", "Maria"]
index=randrange(len(persons))
person=persons[index]
print(person)
print()

persons1=["Alvaro", "Javier", "Veronica", "Martha", "Maria"]
index1=randint(0,len(persons1)-1)
person1=persons1[index1]
print(person1)
print()

#random
d=random()
print(d)
print()

#uniform
e=uniform(0,10)
print(e)
print()

#choice
stundent="axell"
word=choice(stundent)
print(word)
print()

stundents=["Axell", "Karla", "Beatriz", "Bryan", "Jon"]
element=choice(stundents)
print(element)
print()

stundents1=["Axell", "Karla", "Beatriz", "Bryan", "Jon"]
element1=sample(stundents,2)
print(*element1)
print()

poker=["A",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
shuffle(poker)
print(poker)
print()





