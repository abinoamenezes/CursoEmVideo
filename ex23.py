m18=0
homem=0
mulher=0
idm=0
sex=None
while True:
    id= int(input('Digite sua idade'))
    if id>18:
        m18= m18 + 1
        sex= str(input('Digite seu sexo: M/F')).upper()
    if sex=='M':
        homem= homem + 1
    elif sex=='F':
        mulher=mulher +1
        if id<20:
            idm=idm+1
    print ('Cadastro realizado com sucesso ')
    cont= str(input('Quer continuar S/N?')).upper()
    if cont=='N':
        break
print (f'{homem} homens foram cadastrados\n {m18}  pessoas possuem mais que  18 anos\n {mulher} mulheres foram cadastradas e {idm} possuem menos de 20 anos ')

