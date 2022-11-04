lis=list()
c=0
lis.append(str(input('digite um número')))
res=str(input('Quer continuar: S/N')).upper()
c=c+1
while res=='S':
    lis.append(str(input('digite um número')))
    res = str(input('Quer continuar: S/N')).upper()
    c=c+1
    if res =='N':
        break
lis.sort(reverse=True)
print (f'A quantidade de números digitados foi {c}')
print (f'A lista digitada de forma decrescente é {lis}')
if '5' in lis:
    print ('o numero 5 está na lista')
else:
    print ('O numero 5 não está na lista')

