"""
PROBLEM 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""


i=0
tot=0
for i in range (1000):
    #Add all multiples of 3 less than 100
    if (i%3 ==0):
        tot+=i
    #Add all multiples of 5 less than 100
    if (i%5 ==0):
        tot+=i

    #Multiples of 15 coounted twice rectiy with this
    if (i%15==0):
        tot-=i
            
print(tot)
    
