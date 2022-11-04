import re
import os
os.system('cls')


class Paciente:
    def __init__(self,nome, idade,doenca,gravidade):
        self.nome=nome
        self.idade=idade
        self.doenca=doenca
        self.gravidade=gravidade

    def dados(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'Doença: {self.doenca}')
        print(f'Gravidade: {self.gravidade}')


while True:
    resposta=input('Deseja adicionar algum paciente? SIM/NAO: ').upper()
    if resposta=='SIM':
        paciente=Paciente(input('Digite o nome do paciente: '),input('Digite a idade do paciente: '),input('digite a Doença: '),
        input('Digite o estado do paciente: '))
        paciente.dados()
        if int(paciente.idade)>65 and paciente.gravidade=='grave':print('paciente com idade avançada e em estado grave , recomanda-se que vá diretamente para sala vermelha')
        elif int(paciente.idade)>65 and paciente.gravidade=='médio' or paciente.gravidade=='lleve':
            print('paciente precisa de atenção, pois mesmo não está com problemas graves, já é idoso')

    else:
        break
