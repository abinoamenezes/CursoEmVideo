frase=str(input (' digite uma frase: '))
frase= frase.split()
frase= ''.join(frase)
normal=frase
t=0
c=-1
for c in range (-1,-1-len(frase),-1):
    print (frase[c],end='')
    if frase[c]==frase[-c-1]:
        t=t +1
print ('')
if t== len(frase):
    print (' é polindrom')
else:
    print ('nao é polindromo')







