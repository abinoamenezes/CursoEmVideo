n=int(input())
def fibon (n):
    if n==0:
        return 'b'
    elif n==1:
        return 'a'
    else:
       return fibon (n-1) + fibon(n-2)
print (fibon(n))


