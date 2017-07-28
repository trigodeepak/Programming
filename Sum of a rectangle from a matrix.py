#Sum query immutable 2d array
a=[[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]]
n = 5#row length +1
c = [[0 for i in range(n)]for x in range(n)]
for i in range(n):
    for j in range(n):
        if(i==0 or j==0):
            continue
        else:
            c[i][j] = c[i-1][j]+c[i][j-1]+a[i-1][j-1]-c[i-1][j-1]
for i in c:
    print i
# To do a query lets provide 2 values
r1 = 2
c1 = 2
r2 = 4
c2 = 3
#Sum from 2,2 to 4,3
print c[r2][c2]-c[r1-1][c2]-c[r2][c1-1]+c[r1-1][c1-1]
    
