""" prime numbers v3
AR
with function
2, 3, 5, 7, 11, 13, 17, 19, 23 ..."""
import math
# function
def isprime(k):
    if k==2:
        return True
    for i in range(2, k):
        if k%i==0:
            return False
            break
    return True
       
while True:
    n=int(input('Insert a natural number bigger than one: '))
    if n>1:
        break
if isprime(n) is True:
    print('The number is  prime ')
else:
    print('The number isnt  prime ')