def MDC(a,b):
    if a==b==0:
        return 'Indeterminado'
    elif b==0:
        return a
    else:
        return  MDC(b, a%b)
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
x=MDC(a,b)
print(f'O MDC de {a} e {b} é {x}')