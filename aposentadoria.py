nome={'nome': str(input('Digite seu nome: ')),
      'idade': 2022- (int(input('Digite o ano que voçe nasceu: '))),
      'CTPS': int(input('Digite sua carteira de trabalho: '))}

if nome['CTPS']!=0:
    nome['Ano de contratação']=int(input('Digite o ano da sua contratação: '))
    nome['salário']=float(input('Digite o seu salário: '))
    print(f'Voçê ira se aposentar em {nome["Ano de contratação"] + 35} com {nome["idade"] + 35} anos ')
else:
    print('FIM')



