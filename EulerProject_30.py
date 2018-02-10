referenceList = [x**5 for x in range(0,10)]
print(referenceList)

def digitFifthSum(n):
    sum=0
    while n >0:
        m = n % 10 
        sum+= referenceList[m]
        n= int(n/10)

    return sum

fifthSums=[]
for i in range(32,5000000):
    if i == digitFifthSum(i):
        fifthSums.append(i)

print(fifthSums)
print(sum(fifthSums))
