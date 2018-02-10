"""
d1 x d10 x d100 x d1000 x d10000 x d100000
"""


numString=" "
for i in range(1,500000):
    numString = numString + str(i)

product=1
product *= int(numString[1])
product *= int(numString[10])
product *= int(numString[100])
product *= int(numString[1000])
product *= int(numString[10000])
product *= int(numString[100000])
product *= int(numString[1000000])

print(product)


            
