import os
os.system('cls')
class Pokemon:
    def __init__(self,nome,natureza,ataque,defesa):
        self.nome=nome
        self.natureza=natureza
        self.poder_ataque=ataque
        self.poder_defesa=defesa
    
    def mostrar_dados(self):
        print('Dados... ')
        print(self.nome)
        print(f'tipo: {self.natureza}')
        print(f'ataque: {self.poder_ataque}')
        print(f'defesa: {self.poder_defesa}')

pokemon1=Pokemon('Pikachu', 'Eletrico', 50,30)
pokemon2=Pokemon('charmander', 'fogo',100,50)
pokemon1.mostrar_dados()
print()
pokemon2.mostrar_dados()



