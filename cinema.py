lugares=[10,2,1,3,0]
sal=[]

while True:
    sala=int(input('Digite a sala(0 sai): '))
    if sala==0:
        print ('fim')
        break
    if sala>len(lugares) or sala<1:
        print('saída inválida')
    elif lugares[sala-1]:
        print('Desculpas, sala lotada')
    else:
        reser=int(input(f'Quantos lugares deseja reservar? lugares disponíveis: {lugares[sala-1]}'))
        if reser>lugares[sala-1]:
            print('Erro, número  superior ao número de lugares disponíveis')
        elif reser<0:
            print('é necessário reservar pelo menos uma cadeira')
        else:
            lugares[sala-1]-=reser
            print('Lugares reservados com sucesso' )
for c,x in enumerate(lugares):
    print(f'sala{c+1} está com {x} lugares disponíveis')













