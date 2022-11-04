import random
m= []
for i in range(0,3):
    m.append([0]*3)
for c in range (3):
    for j in range (3):
        m[c][j]= random.randint(0,9)
for c in range (3):
    print (m[c])
    print ('',end='')

