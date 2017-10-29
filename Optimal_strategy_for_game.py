#programming for optimal strategy for a game
a = [3,9,1,2]
n = len(a)
c = [[[0,0] for i in xrange(4)]for x in xrange(4)]
k = 0
while(k<n):
    i = 0
    j = k
    while(j<n):
        print i,j
        for m in c:
            print m
        if i == j:
            c[i][j] = [a[i],0]
        else:
            if (c[i+1][j][1]+a[i])>(c[i][j-1][1]+a[j]):
                c[i][j][0] = c[i+1][j][1]+a[i]
                c[i][j][1] = c[i+1][j][0]
            else:
                c[i][j][0] = c[i][j-1][1]+a[j]
                c[i][j][1] = c[i][j-1][0]
        j+=1
        i+=1
    k+=1
for i in c:
    print i
