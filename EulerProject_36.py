def isPallindromic(number):
    strNumber=str(number)
    if strNumber == strNumber[::-1]:
        return True
    else:
        return False

def binConverter(n):
    binString = bin(n)
    return binString[2:]

totalSum = 0
for i in range(1,1000000):
    binNum = binConverter(i)
    if isPallindromic(i) and isPallindromic(binNum):
        totalSum+=i
    else:
        continue

print(totalSum)
