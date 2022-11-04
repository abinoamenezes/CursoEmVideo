def distancia(lss):
    menor = 0

    for tupla in lss:
        g = len(tupla)
        c = 0
        total = abs(mapa['R'][0] - mapa[tupla[c]][0]) + abs(mapa['R'][1] - mapa[tupla[c]][1])
        while c < g - 1:
            total = total + abs(mapa[tupla[c]][0] - mapa[tupla[c + 1]][0]) + abs(
                mapa[tupla[c]][1] - mapa[tupla[c + 1]][1])
            c = c + 1
        total = total + abs(mapa['R'][0] - mapa[tupla[c]][0]) + abs(mapa['R'][1] - mapa[tupla[c]][1])
        if total < menor or menor == 0:
            menor = total
            rota = tupla
    print(f'Menor distância: {menor} dronômetros')
    rota = ' '.join(rota)  # transformando tupla em string
    print(f'Rota com a menor distância: {rota}')

# chamando função

distancia(combinacao)
