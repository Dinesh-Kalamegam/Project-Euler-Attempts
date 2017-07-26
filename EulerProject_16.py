#Digit Sum found by accumulating each mod 10 
def addDigit(n):
    digitSum = 0
    while n!=0:
        digitSum += n % 10
        n //= 10
    return digitSum

print(addDigit(2**1000))
