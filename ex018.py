n=None
nd=0
soma=0
while n!=999:
    n = int(input('digite um numero: '))
    if n != 999:
        nd= nd + 1
        soma= soma + n
print (' A quantidade de números digitados foi {} e a soma entre eles é {}'.format(nd,soma))