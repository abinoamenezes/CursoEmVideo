from itertools import permutations

rota = []
mapa = {}
lis = []
pontos = []
a = list()
file = open('matriz', 'r')  # abrindo arquivo
linhas = file.readlines()
for c in linhas[0]:
    lin = c
    colu = c

# criando matriz
for l in linhas:
    con = l.split()
    lis.append(con)
del lis[0]
# descobrindo posições

for c in lis:
    x = len(c)
    for j in range(x):
        if c[j] != '0':
            mapa[c[j]] = (lis.index(c), j)
            if c[j] != 'R' and c[j] != '0':
                pontos.append(c[j])
# oermutações
p = list(permutations(pontos))


def distancia(lss):
    menor = 0

    for i in lss:
        g = len(i)
        c = 0
        t = 0
        r = abs(mapa['R'][0] - mapa[i[c]][0]) + abs(mapa['R'][1] - mapa[i[c]][1])
        while c < g - 1:
            y = abs(mapa[i[c]][0] - mapa[i[c + 1]][0]) + abs(mapa[i[c]][1] - mapa[i[c + 1]][1])
            r = r + y
            c = c + 1
        t = r + abs(mapa['R'][0] - mapa[i[c]][0]) + abs(mapa['R'][1] - mapa[i[c]][1])
        # print(t)
        if t < menor or menor == 0:
            menor = t
            rota = i
    print(menor)
    print(rota)


# distância

distancia(p)
