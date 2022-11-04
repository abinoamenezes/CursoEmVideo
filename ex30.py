lis = list()
c = None
while True:
    c = int(input('digite um valor inteiro para ser adicionado na lista: '))
    while c in lis:
        print('valor ja adicionado.', end='')
        c = int(input('digite um valor inteiro para ser adicionado na lista: '))
    print('valor adicionado')
    lis.append(c)
    res = str(input('voçê quer continuar?:  S/N')).upper()
    if res == 'N':
        break
lis.sort()
print(f'a lista que que voçe digigitou é {lis}')
