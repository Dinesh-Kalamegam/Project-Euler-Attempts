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
            

counter = 1
j=3
while(True):
    iPrime = str(isPrime(j))

    if(isPrime(j) == True):
        counter+=1

    if (counter == 10001):
      print(j)
      break

    j+=2
    
