#Program for cutting rod problem (something like knapsack)
a = [2,5,7,8]
n = 5
c = [[0 for i in xrange(n+1)]for x in xrange(len(a)+1)]

for i in xrange(len(a)+1):
    for j in xrange(n+1):
        if (i==0 or j==0):
            continue
        elif(i<=j):
            c[i][j] = max(c[i-1][j],c[i][j-i]+a[i-1])
        else:
            c[i][j] = c[i-1][j]
        
for i in c:
    print i
# The answer is 12 in this case
        
