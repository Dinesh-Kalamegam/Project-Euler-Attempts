#square each number from 1 to n and square them 
def squareSum(n):
    result=0
    for i in range (1,n+1):
        result+= i**2
    return result
        
#square the sum of the numbers from 1 to n
def sumSquare(n):
    result=0
    for j in range (1,n+1):
        result += j
    result = result **2
    return result

#Find the absolute value for the difference between them 
def dif(a,b):
    result = abs(a-b)
    return result
