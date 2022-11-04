from math import floor
def exp(a,n):

    if n==0:
        return 1
    else:
        return a * exp(a,n-1)

def expmod(a,n,m):
    if a==n==0:
        return 'impossível de calcular'
    if n==0:
        return 1
    elif n % 2==0:
        return exp(expmod(a,n/2,m),2) % m
    else:
        return (((exp((expmod(a,floor(n/2),m)),2) % m) * a%m))%m

a=int(input('Digite a base: '))
n=int(input('Digite o expoente: '))
m=int(input('Digite o módulo: '))
x=expmod(a,n,m)
print(f'exponecial modular é :  {x}')