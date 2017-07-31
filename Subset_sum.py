#Program to find subset sum from a given set similar to knapsack
a = [2,3,7,8,10]
n=11
c = [[False for i in xrange(n)]for x in xrange(len(a)+1)]
c[0][0] = True
for i in xrange(1,len(a)+1):
    for j in xrange(n):
        if (j==0):
            c[i][j] = True
        elif(j==a[i-1]):
            c[i][j] = True
        else:
            c[i][j] = c[i-1][j-a[i-1]]
for i in c:
    print i

#The answer is true in this case

