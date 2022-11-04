pt=int(input('digite o primeiro termo: '))
rz=int(input('digite a razao: '))
c=1
r=None

while c<11:
    pa= pt + rz
    pt=pa
    c=c + 1
    print (pa)
r =str(input('Quer que seja mostrado mais algum termo ? S/n'))
if r=='s':
    ter=int(input('Quantos mais termos quer mostrar: ?'))
    c=1
    while c<ter:
        tr= pa + rz
        pa=tr
        print (tr)
        c=c+1








