from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador1': randint(1,6),
      'jogador2':randint(1,6),
      'jogador3': randint(1,6),
      'jogador4':randint(1,6)}
rank={}
for k,c in jogo.items():
    print(f'{k} tirou {c}')
    sleep(0.8)
rank=sorted(jogo.items(), key=itemgetter(1),reverse=True)

for k,c in enumerate(rank):
    print(f'o {k+1} lugar foi de {c[0]} que tirou {c[1]}')
    sleep(0.8)