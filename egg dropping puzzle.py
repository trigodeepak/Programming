#Program
def result(a,n):
    c = [[0 for i in range(n+1)] for j in range(a+1)]
    for i in range(n):
        c[1][i+1] = i+1
    for i in range(2,a+1):
        for j in range(n+1):
            if i > j:
                c[i][j] = c[i-1][j]
                continue
            m = float('inf')
            for k in range(1,j+1):
                r = max(c[i-1][k-1],c[i][j-k])
                m = min(m,r)
                # print(i,j,k,r)
            c[i][j] = 1+m
    print(c[a][n])
t = int(input())
for _ in range(t):
    e,n = list(map(int,input().split()))
    (result(e,n))
# Sample input
# 1
# 2 10
