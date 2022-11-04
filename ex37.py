matriz=[]
for c in range (3):
    matriz.append([0]*3)
for c in range (3):
    for j in range (3):
        d=int(input(f'Digite o valor para ser adicionado na posição {c},{j}: '))
        matriz[c][j]=d
print (matriz)
