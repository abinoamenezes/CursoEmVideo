simbAbre='({['
simbFecha=')}]'
p,c,ch='()','{}','[]'
pilha=[]


def procedimento_verifica(string):
    global pilha
    for simb in string:
        if simb in simbAbre: pilha.append(simb)
        elif simb in simbFecha:
            if len(pilha)>0:
                y=pilha.pop()
                soma= y + simb
                if soma not in p and soma not in c and soma not in  ch: return 'casamento imperfeito'
            else:
                return 'casamento imperfeito'
    
    if len(pilha)==0: return 'casamento perfeito'
    else:
        return 'casamento imperfeito'

string= str(input())
print(procedimento_verifica(string))