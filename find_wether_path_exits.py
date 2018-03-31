row = [1,0,-1,0]
col = [0,1,0,-1]
def isValid(r,c,n):
    if 0<=r<n and 0<=c<n:
        return True
    return False
    
def result(a,n,i,j):
    # print (i,j)
    visited[i][j] = True
    if a[i*n+j] == 2:
        return True
    for k in range(4):
        r = i+row[k]
        c = j+col[k]
        if isValid(r,c,n) and not visited[r][c] and a[i*n+j]:
            if a[i*n+j] == 2 or result(a,n,r,c):
                return True
    return False         
    
t = int(input())
visited =[]
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    visited = [[False for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i*n+j] == 1:
                res = (result(a,n,i,j))
                break
    if (res):
        print (1)
    else:
        print (0)
    t-=1
