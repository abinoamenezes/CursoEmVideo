import random
pontos=0
vc= None
while True:
    nal= random.randint(0,10)
    vd= int(input('digite um valor: '))
    pi= str(input('Par ou impar ? p/i'))
    if pi=='p':
       sn= vd+nal
       if sn%2==0:
           print (f'o numero que voçe escolheu foi {vd}, o jogo esolheu {nal}, ou seja {sn} é par ')
           print ('voçe venceu')
           pontos=pontos +1
       elif sn%2!=0:
           print (f'o número que voçe escolheu foi {vd}, o jogo escolheu {nal}, ou seja {sn} é impar')
           print('voçê perdeu')
           vc='perdeu'
    elif pi=='i':
        sn= vd + nal
        if sn%2!=0:
            print (f'o Número que voçê escolheu foi {vd},o jogo escolheu {nal}, ou seja {sn } é impar')
            print ('voçê venceu')
            pontos=pontos +1
        elif sn%2==0:
            print (f'o número que voçê escolheu foi {vd} o jogo escolheu {nal}, ou seja {sn} é par')
            print ('voçe perdeu')
            vc='perdeu'
    if vc=='perdeu':
        break
print ('fim de jogo')
print (f'voçê venceu {pontos} vezes')






