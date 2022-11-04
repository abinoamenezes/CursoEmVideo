o=list()
f=list()
r='S'
pp=list()
pl=list()
pessoas=0
while r=='S':
    f.append(str(input('digite o seu nome')))
    pessoas=pessoas+1
    f.append (int(input('Digite seu peso')))
    if f[1]>=100:
         pp.append(f[0])
    elif f[1]<100:
        pl.append(f[0])
    o.append(f[:])
    f.clear()
    r = str(input('Quer continuar? S/N')).upper()
    if r=='N':
        break
print (f'{pessoas} foram cadastradas\n as pessoas que estão acima do peso saõ {pp}\n as que estão abaixo do peso são {pl}')

