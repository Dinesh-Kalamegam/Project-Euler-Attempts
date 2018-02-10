import math
import time 

def isPrime(n):
    sqrtN = math.floor(math.sqrt(n))

    if (n<=1):
        return False

    elif (n ==2):
        return True
    
    
    else:
        for i in range(3,sqrtN+1,2):
            if((n%i) ==0):
                return False
            else:
                continue

        return True

sumPrime =2

j=3
while(j<2000000):
    if(isPrime(j) == True):
        sumPrime += j

    j+=2

print(sumPrime)
        
