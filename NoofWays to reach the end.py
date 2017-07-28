#Total number of ways to reach at the end in a matrix using dp
n = 4
c = [[1 for i in range(n)] for x in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            continue
        else:
            c[i][j]= c[i-1][j] + c[i][j-1]
for i in c:
    print i
