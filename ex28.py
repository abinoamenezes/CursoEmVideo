d=(int (input('digite um valor: '))),(int (input('digite um valor: '))),(int (input('digite um valor: '))),(int (input('digite um valor: '))),(int (input('digite um valor: ')))
print (f'o valor 9 apareceu {d.count(9)} vezes')
print (f'o valor 3 foi digitado na posição {d.index(3)}')
print ('os numeros pares são ', end=' ')
for n in d:
    if n%2==0:
        print (n,end=' ')