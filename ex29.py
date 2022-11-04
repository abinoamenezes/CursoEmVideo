menor= None
valor= list()
maior=0
pos=list()
posm=list()
for c in range (0,5):
    valor.append(int(input(f'digite um valor inteiro na posição {c}: ')))
for r,n in  enumerate(valor):
    if r==0:
        menor=n
    if n >= maior:
        maior=n
    if n<menor:
        menor=n
for c,t in enumerate (valor):
    if t==maior:
        pos.append(c)
    elif t== menor:
        posm.append(c)
print (f'a lista é {valor}\n  o maior valor da lista è {maior} e está nas posições {pos} o menor número é {menor} e está nas posições {posm}')


