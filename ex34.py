princ=list()
par=list()
impar=list()
for c in range  (0,6):
    x=int(input('digite um número: '))
    if x%2==0:
        par.append(x)
    else:
        impar.append(x)
princ.append(par)
par.sort()
princ.append(impar)
impar.sort()
print (princ)


