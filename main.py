n1= int(input('digite o 1 lado do triângulo '))
n2= int(input('Digite o lado 2 do triango '))
n3= int(input('digite o lado 3 do triângulo'))
if n1==n2 and n2==n3:
    print('O triângulo é equilatero')
elif n1==n2 or n2== n3 or n1==n3:
    print ('O triângulo é isosceles')
else:
    print('Triângulo escaleno')