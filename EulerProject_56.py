def addDigit(n):
    digitSum = 0
    while n!=0:
        digitSum += n % 10
        n //= 10
    return digitSum

maxDigSum=0
for a in range (1,100):
    for b in range(1,100):
        #print("a is " + str(a) + " and b is " + str(b))
        #print("the digit sum of power is " + str(addDigit(a**b)) +"\n")
        digSum=addDigit(a**b)
        if addDigit(a**b)>maxDigSum:
            maxDigSum=digSum
        else:
            continue

print(maxDigSum)
