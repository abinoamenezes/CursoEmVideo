x= float(input())
res=0
cal=1
for n in range (0,50):
    c= (-1)**n
    d= 2*n
    if d>0:
        fator=1
        t=d
        while t>0:
            fator= fator*t
            cal=fator
            t=t-1
    cos =x**(2*n)
    res=res + (c/cal *cos)
print (f'{res:.4f}')










