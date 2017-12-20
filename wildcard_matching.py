#wildcard matching
a = list('baaabab')
p = list('*****ba*****ab')
i = 0
while(i<len(p)):
    if p[i] == '*':
        while p[i+1] == '*':
            p.pop(i+1)
    i+=1
print p
m = len(p)
n = len(a)
c = [[False for i in xrange(m+1)] for x in xrange(n+1)]
c[0][0] = True
if p[0] == '*':
    for i in xrange(m+1):
        c[0][i] = True
i = 1
while i<n+1:
    j = 1
    while j<m+1:
        #print i,j,a,p
        if p[j-1] == '?' or p[j-1] == a[i-1]:
            c[i][j] = c[i-1][j-1]           
        elif p[j-1] == '*':
            c[i][j] = c[i][j-1] or c[i-1][j]           
        elif p[j-1] != a[i-1]:
            c[i][j] = False
        j+=1
    i+=1
for i in c:
    print i
            
