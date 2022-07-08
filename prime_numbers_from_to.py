def prime_numbers_from_to(n):
    for n in range(2,n+1):      
        counter=0
        i=2
        while counter==0 and i<n:
            prime=n%i
            #print(n,i,prime)
            if prime==0:
                counter+=1
            i+=1       
        if counter==0:
            print(n, end=" ")
prime_numbers_from_to(100)
