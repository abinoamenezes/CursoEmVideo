import random
l=int(input('Digite a quantidades de linhas '))
c=int(input('Digite a quantidade de colunas'))
matriz=[]
for c in range (l):
    matriz.append([0]*l)
for j in range(l):
    for i in range (l):
        matriz[j][i]= random.randint(0,9)
for c in matriz :
    print (c)
    print (end='')


