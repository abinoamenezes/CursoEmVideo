res = 'S'
lis = list()
qp = 0
si = 0
mulheres = []
maiores=[]
while res == 'S':  # dicionario inicial
    dic = {'Nome': str(input('Digite seu nome: ')),
           'idade': int(input('Digite sua idade')),
           'Sexo': str(input('Digite seu sexo M/F: ')).upper()}
    qp = qp + 1
    lis.append(dic.copy())
    res = str(input('Quer continuar S/N')).upper()
    if dic['Sexo'] == 'F':  # lista so das mulheres
        mulheres.append(dic['Nome'])
for c in lis:  # media das idades
    si = si + c['idade']
media = si / qp
for c in lis:
    if c['idade']>media:
        maiores.append(c['Nome'])
print(f'A média de idade do grupo é {media}')
print(f'A quantidade de pessoas cadastradas foi {qp}')
print(f'Mulheres cadastrada {mulheres}')
print(f'As pessoas com a idade acima da média é {maiores}')
