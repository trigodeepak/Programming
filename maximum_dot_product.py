#Find maximum dot product for 2 arrays by inserting 0's in second array
a = [2, 3 , 1, 7, 8]
b = [3, 6, 7]
n = len(b)
m = len(a)
c = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
for i in xrange(1,n+1):
    for j in xrange(1,m+1):
        c[i][j] = max(c[i-1][j-1]+a[j-1]*b[i-1],c[i][j-1])
for i in c:
    print i
        
print "Answer is : ",c[n][m]
