lis=list()
lisp=list()
lisi=list()
x=int(input('digite um número inteiro'))
lis.append(x)
res=str(input('Quer continuar? S/N')).upper()
while res=='S':
    x=int(input('digite um número inteiro'))
    lis.append(x)
    if x % 2==0:
        lisp.append(x)
    else:
        lisi.append(x)
    res = str(input('Quer continuar? S/N')).upper()
    if res=='N':
        break
print (f' Lista original: {lis}\n lista com pares {lisp}\n lista com impares {lisi}')

