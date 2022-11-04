nu=int(input('digite um número'))
menor=nu
res='s'
soma=nu
c=1
maior=nu
while res=='s':
    nu=int(input('digite um número'))
    if nu>maior: maior=nu      
    if nu<menor:
        menor=nu

    soma= soma + nu
    c=c+1
    res= str(input('Quer continuar?: s/n'))
media=soma/c
print ('A média entre os vaores digitados é {}, o maior número digitado foi {}, o menor número digitado foi {}'.format(media,maior,menor))


