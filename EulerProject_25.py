def countDigits(n):
    stringN = str(n)
    return len(stringN)

i=3
fibNums =[1,1,2,3]
for i in range(3,10000,1):
    fibNums.append(fibNums[i]+fibNums[i-1])
    if (countDigits(fibNums[i]) ==1000):
        #If array starts at 0 then the index in sequence is i+1
        print(i+1)
        break
    else:
        continue
