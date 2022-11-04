import os
import json
os.system('cls')
dic={
    'nome':'Abinoa',
    'idade':20,
    'cidade':'Igarassu',
    'carros': [
        {'Marca':'BMW','Ano':2021},
        {'Marca':'Jaguar','Ano':2022}
    ]
}
print(json.dumps(dic,indent=4))