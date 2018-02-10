def collatzChain(n):
    lengthChain=0
    while n!=1:
        if n%2==0:
            n=int(n/2)
        else:
            n=int((3*n)+1)
        print(n)

def collatzChainLength(n):
    lengthChain=0
    while n!=1:
        if n%2==0:
            n=int(n/2)
        else:
            n=int((3*n)+1)
        #print(n)
        lengthChain+=1
    return lengthChain

maxChainLength=0
maxChainValue=0
for i in range(100,1000000):
    chainLength = collatzChainLength(i)
    if maxChainLength < chainLength:
        maxChainLength = chainLength
        maxChainValue = i 
    else:
        continue


print(maxChainValue)
