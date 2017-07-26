import time

#recursive function for factorial 
def fac(n):
    if (n==0):
        return 1
    else:
        return n * fac(n-1)
    
#Digit Sum found by accumulating each mod 10 
def addDigitFac(n):
    digitSum = 0
    while n!=0:
        index =(n%10)
        digitSum += factorials[index]
        n //= 10
    return digitSum

#precalculated factorials using the factorial function 
factorials=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
facSum=0

t0=time.clock()
for i in range (3,10000000):
    if(addDigitFac(i)==i):
        facSum+=i
    else:
        continue

