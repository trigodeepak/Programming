#Program for Cutting rod problem
##a = map(int, raw_input().strip().split(' '))
#Not working correctly for some examples
p = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(p)
c = [[0 for i in range(n+2)]for i in range(n)]
for i in range(n+2):
    c[0][i] = p[0]*i
for i in range(1,n):
    for j in range(n+2):
        if(j>i):
            c[i][j]=max(c[i-1][j],p[i]+c[i][j-i-1])
        else:
            c[i][j]=c[i-1][j]
print c
