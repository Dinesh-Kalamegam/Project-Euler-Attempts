#recursive function for factorial 
def fac(n):
    if (n==0):
        return 1
    else:
        return n * fac(n-1)
    
#factorial found iteratively
def fac2(n):
    facRes =1
    for i in range(1,n+1):
        facRes*=i
    return facRes

#Digit Sum found by accumulating each mod 10 
def addDigit(n):
    digitSum = 0
    while n!=0:
        digitSum += n % 10
        n //= 10
    return digitSum

#in terminal wrote addDigit(fac(100))
