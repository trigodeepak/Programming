# Relative sorting using compare function
def compare(a):
    return d[a]
def result(a,n):
    a = sorted(a,key=compare)
    print (' '.join([str(i) for i in a]))
        
from collections import defaultdict
d = defaultdict(int)
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(m):
        d[b[i]] = i
    for i in a:
        if i not in d:
            d[i] = 1001+i#max elements are 1000
    (result(a,n))
    d = defaultdict(int)
