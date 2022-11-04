tabela= ('palmeiras','Corinthians','Internacional','Atlético MG','Fluminense','Athletico PR','São Paulo','Santos','Flamengo','Botafogo','Bragantino','Goias','Cúiaba','Coritiba','America MG','Avái','Ceára','Atletico GO','Juventude','Fortaleza')
print (f'Os 5 primeiros colocados são {tabela[:5]}\n os 4 últimos colocados são {tabela [16:]}')
print (sorted(tabela))
print (f'O corinthians está na posição {tabela.index("Santos")} ')