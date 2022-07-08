def prime_numbers_from_to(n):
    for primes in range(2,n+1):
        counter=0
        i=2
        while counter==0 and i<n:
            prime=n%i
            #print(n,i,prime)
            if prime==0:
                counter+=1
            i+=1

        if n<=1:
            print("Please introduce a number bigger than 1")
        
        elif counter==0:
            print(n, "es numero primo")
        
        else:
            print(n, "no es numero primo")

prime_numbers_from_to(17)
