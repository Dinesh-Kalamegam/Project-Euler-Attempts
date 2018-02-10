import math

def factorisePrime(n):
    while n%2 == 0:
        n = n/2

    for i in range (3, (int(math.sqrt(n)))+1,2):
        while n%i == 0:
            print (int(i))
            n=n/i

    if n>2:
        print(n)
    
        
factorisePrime(600851475143) 
