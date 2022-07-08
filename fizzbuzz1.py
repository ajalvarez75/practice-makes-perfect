def words(numbers):
    a=[]
    for i in range(1,numbers):
        if i%3==0 and i%5==0:
            a.append("fizzbuzz")
        elif i%3==0:
            a.append("fizz")
        elif i%5==0:
            a.append("buzz")
        else:
            a.append(i)
    print(a)

words(101)