#Prime numbers v2
# AR
# iterate just  uo to sqrt(n)
#2, 3, 5, 7, 11, 13, 17, 19, 23
#   suppose that n=a*b and  a<b (*a) and (*b)
# a^2<a*b
# a*b<b^2
#a^2<n<b^2
#a<sqrt(n)<b
import math
while True:
    n=int(input('Insert a natural number bigger than one: '))
    if n>1:
        break
# assume the value is prime
prime=True
# define initial quocient
quocient=2
#computation
# if  is divisible by any number in the interval 2.. n-1 is not a prime
while  quocient<=math.sqrt(n):
    remain=n%quocient
    if remain==0:
        prime=False
        break
    quocient+=1
#output
if prime==False:
    print('The number is not prime ')
else:
    print('The number is  prime ')