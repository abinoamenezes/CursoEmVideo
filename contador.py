from time import sleep
def contador(i,f,p):
    for c in range(i,f,p):
        print (c, end='')
        sleep(0.5)
    print('')
    for c in range(f,i,-p):
        print(c,end='')
        sleep(0.5)

i=int(input('Digite o inicio da contagem: '))
f=int(input('digite o fim da contagem: '))
p=int(input('digite o passo: '))
contador(i,f,p)