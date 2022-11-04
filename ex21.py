while True:
    c=0
    nt=int(input('Digite um número para ver sua tabuada'))
    if nt<0:
        break
    while c<11:
        print (f'{nt} x {c} = {nt*c}')
        c=c+1
print ('fim')