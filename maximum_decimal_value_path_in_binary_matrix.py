#Program for Maximum decimal value path in a binary matrix
a = [[1 ,1 ,0 ,1],[0 ,1 ,1 ,0],[1 ,0 ,0 ,1],[1 ,0 ,1 ,1]]
n = len(a)
m = len(a[0])
c = [[0 for i in xrange(m+1)]for x in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(m+1):
        if i == 0 or j == 0:
            continue
        elif a[i-1][j-1] == 1:
            c[i][j] = 2**(i-1+j-1) + max(c[i-1][j],c[i][j-1])
        else:
            c[i][j] = max(c[i-1][j],c[i][j-1])
for i in c:
    print i
            
