row = [-1,1,0,0]
col = [0,0,-1,1]

def isvalid(r,c,n,m):
    if (0<=r<n and 0<=c<m):
        return True
    return False

def bfs(a,u,m):
    res = {}
    visited = [[False for i in range(m)] for j in range(u)]
    queue = []
    count = 0
    for i in range(u):
        for j in range(m):
            if a[i*m+j] == 2:
                queue.append([i,j,0])
                visited[i][j] = True
                count-=1
            if a[i*m+j] != 0:
                count+=1
    cnt = -1
    while len(queue) > 0:
        q = len(queue)
        cnt+=1
        for k in range(q):
            n = queue.pop(0)
            for i in range(4):
                r = n[0] + row[i]
                c = n[1] + col[i]
                if (isvalid(r,c,u,m) and a[r*m+c]==1 and not visited[r][c]):
                    visited[r][c] = True
                    queue.append([r,c,n[2]+1])
                    count-=1
    if not (count):
        print (cnt)
    else:
        print (-1)
            
t = int(input())
while t>0:
    n,m = list(map(int,input().split()))
    a = (list(map(int,input().split())))
    bfs(a,n,m)
    t-=1
'''Sample input
2
3 5
2 1 0 2 1 1 0 1 2 1 1 0 0 2 1 
4 7
0 1 2 2 2 1 1 1 0 0 2 1 1 0 0 1 2 1 1 1 0 1 0 1 0 2 0 2
'''
