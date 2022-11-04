def fatorial(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
     return   n * fatorial(n-1)

n=int(input('Digite um número: '))
x=fatorial(n)
print(f'O fatoria de {n} é {x}')