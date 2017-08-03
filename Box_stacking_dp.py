#Program for Box stacking 
a = [1,2,4]
b = [3,2,5]
import itertools
from operator import itemgetter
d = []
for i in itertools.permutations(a):
    i = list(i)
    i.append(i[0]*i[1])
    d.append(i)
for i in itertools.permutations(b):
    i = list(i)
    i.append(i[0]*i[1])
    d.append(i)
print d

d = sorted(d, key=itemgetter(3),reverse=True)
print d
# The answer is 12 in this case
        
