import re
import time
begin=time.time()
st='Brasil será campeão em 2022'
x=re.findall('[arm]',st)
print(x)
print(time.time()-begin)