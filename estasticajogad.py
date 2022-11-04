gols=[]
dic={}
res='S'
while res=='S':
    nome=str(input('Digite o nome do jogador: '))
    partidas=int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols marcou na partida {c+1}: ')))
    dic['Nome']=nome
    dic['Partidas']=partidas
    dic['Gols']=gols
    dic['Total']=sum(gols)
    res=str(input('Quer continuar ? S/N')).upper()
print(f'O jogador {nome} jogou {partidas} partidas')
for c in range(partidas):
    print(f'Na partida {c +1} fez {gols[c]} gols')
print(f'Fez {dic["Total"]} gols no total.')