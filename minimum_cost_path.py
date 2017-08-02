#Program for minimum cost path
a = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]
n = len(a[0])
m = len(a)
c = [[0 for i in xrange(n)]for x in xrange(m)]

for i in xrange(m):
    for j in xrange(n):
        if(i==0 and j==0):
            c[i][j] = a[i][j]
        elif i==0:
            c[i][j]= c[i][j-1] + a[i][j]
        elif j==0:
            c[i][j]= c[i-1][j] + a[i][j]
        else:
            c[i][j] = a[i][j]+min(c[i-1][j],c[i][j-1])
        
for i in c:
    print i
# The answer is 12 in this case
        
