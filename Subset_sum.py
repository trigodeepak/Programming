#Program to find subset sum from a given set similar to knapsack
a = [1,2,3]
a.sort()
n=6
c = [[False for i in range(n)]for x in range(len(a)+1)]
c[0][0] = True
for i in range(1,len(a)+1):
    for j in range(n):
        if (j==0):
            c[i][j] = True
        if (j<a[i-1]):
            c[i][j] = c[i-1][j]
        elif(j==a[i-1]):
            c[i][j] = True
        else:
            c[i][j] = c[i-1][j-a[i-1]]
for i in c:
    print i

#The answer is true in this case

