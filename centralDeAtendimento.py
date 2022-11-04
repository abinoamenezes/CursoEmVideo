import re
x='Ai é foda mesmo né meu camarada'
y=re.search('é',x)
print(y.group())
