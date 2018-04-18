#Program repeating terms
def result(a,n):
    d = {}
    quo = []
    i = 0
    b = a
    while a:
        r = a%n
        q = a//n
        quo.append(str(q))
        if r == 0:
            return ''.join(quo)
        if str(r) not in d:
            d[str(r)] = i
        else:
            break
        a = r
        if a<n:
            if '.' not in d:
                i+=1
                d['.']  = i
                quo.append('.')
            a*=10
        while  a!=0 and a<n:
            quo.append('0')
            a*=10
        i+=1
    ind = d[str(r)]+1
    if quo[ind] == '.':
        ind+=1
    num = (''.join(quo[:ind])+'('+''.join(quo[ind:])+')')
##    print (quo,d)
    return num
##    print (quo,quo[quo.index(q):])
    
t = int(input())
while t > 0:
    a = int(input())
    n = int(input())
##    a = list(map(int,input().split()))
    print(result(a,n))
    
    t-=1
