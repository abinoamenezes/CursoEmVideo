matriz=[]
maior=0
soma= somter=0
for n in range (3):
    matriz.append([0]*3)
for l in range (3):
    for c in range (3):
        matriz[l][c]= int(input(f'digite um numero na posição {l},{c}: '))
        if (matriz[l][c]) % 2==0:
            soma=soma + matriz[l][c]
        if c==2:
            somter=somter + matriz[l][c]
    if l==1:
       if  matriz[l][c]>maior:
           maior=matriz[l][c]
for c in range (3):
    print (matriz[c])
    print (end='')
print (f'A soma de todos os números pares  dessa matriz é {soma}')
print (f'A soma de todos os números da 3 coluna é {somter}')
print (f'O maior valor na segunda linha é {maior}')