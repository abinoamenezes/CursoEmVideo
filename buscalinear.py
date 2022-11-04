def busca(lis, i, j, x):
    #list(map(str, lis))

    if len(lis) == 0:
        return -1
    elif lis[i] == x:
        return i
    elif lis[i] != x:
        if i < j:
            return busca(lis, i + 1, j, x)
        else:
            return -1


from random import randint

lis = [randint(0, 30) for c in range(15)]


x = int(input('Digite o número que deseja procurar na lista: '))
i = 0
j = len(lis) - 1
res = busca(lis, i, j, x)
print(f'Posição: {res}')
