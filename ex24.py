c=0
c2=0
vp=0

pb=None
while True:
    np=str(input('Digite o nome do produto: '))
    c=c+1
    pp= float(input('digite o preço do produto: '))
    menor=pp
    if menor<=pp:
        menor= pp
        pb= np
    vp= vp + pp
    if pp>1000:
        c2=c2+1
    per= str (input('Quer continuar?: S/N')).upper()
    if per=='N':
        break
print (f'O total gasto na compra foi {vp}\n {c2} produtos custaram mais de 1000\n O produto mais barato foi {pb}')

