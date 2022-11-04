ultimo=10
fila=list(range(1,ultimo+1))
while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'fila atual {fila}')
    print('Digite F para adicionar um cliente no fim da lista ou A para realizar o atendimento. S para sair')
    operacao=str(input('operação (F,A,S): ')).upper()
    if operacao=='A':
        if len(fila)>0:
            atendindo=fila.pop(0)
            print(f'cliente {atendindo} atendindo')
        else:
            print('Impossível de atender pois a fila está vazia')
    elif operacao=='F':
        ultimo+=1
        fila.append(ultimo)
    elif operacao=='S':
        break
    else:
        print('operaçã invalida digite somente (F,A ou S')