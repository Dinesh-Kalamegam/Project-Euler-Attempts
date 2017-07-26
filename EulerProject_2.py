fibNums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
while fibNums[-1]<4000000:
    nextFib=fibNums[-1]+fibNums[-2]
    fibNums.append(nextFib)

print(fibNums)

evenSum=0
for num in fibNums:
    if(num%2 ==0):
        evenSum+=num
    else:
        continue

print(evenSum)
