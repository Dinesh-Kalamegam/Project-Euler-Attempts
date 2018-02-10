import time 

def addSquaresOfDigits(n):
    squareDigitSum=0
    while n:
        squareDigitSum+=(n%10)**2
        n //=10
    return squareDigitSum

def chainMaker(n):
    while n != 1 and n!= 89:
        n=addSquaresOfDigits(n)
    return n 
        
  
def chain89 (n):
    if chainMaker(n)==89:
        return True
    else:
        return False

start=time.time()
arrive89 =0
for i in range(1,10000000):
    if chain89(i)==True:
        arrive89+=1
    else:
        continue
    
print(arrive89)
print("Time taken:" + str(time.time()-start))
