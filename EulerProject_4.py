def checkPal(value):
    """ Function to check if a number is Pallindromic """ 
    stringValue=str(value)
    if stringValue == stringValue[::-1]:
        return True
    else:
        return False

palNums=[]

for i in range (101,1000):
    for j in range(101,1000):
        product=i*j
        if checkPal(product)==True:
            palNums.append(product)
        else:
            continue

sortPalNums=sorted(palNums)
print(sortPalNums[-1])
