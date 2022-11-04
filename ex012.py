m=0
t=0
for c in range(1,8):
    n = int(input('digite o ano que voçê nasceu'))
    if 2022-n>=18:
        m=m+1
    else:
        t= t +1
print ('Das 7 pessoas, {} são de maiores e {} são menores'.format(m,t))