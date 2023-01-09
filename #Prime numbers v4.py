#prime numbers
# AR
# recursion
def isprime(k,i):
    if(k==i):
        return True
    if (k%i==0):      
        return False
    i+=1
    return isprime(k,i)
while True:
    n=int(input('Insert a natural number bigger than one: '))
    if n>=1:
        break
if isprime(n,2):
    print('The number is  prime ')
else:
    print('The number is not prime ')