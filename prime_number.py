def prime_numbers_from_to(n):

    counter=0
    i=2
    while i<n and counter==0:
        prime=n%i
        print(n,i,prime)
        if prime==0:
            counter+=1
        i+=1

    if n<=1:
        print("Please introduce a number bigger than 1")
    
    elif counter==0:
        print(n, "es numero primo")
    
    else:
        print(n, "no es numero primo")

prime_numbers_from_to(9)
