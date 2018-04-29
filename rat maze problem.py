#Program for rat in maze problem
r = [-1,1,0,0]
c = [0,0,-1,1]
visited = []
res = []
ans =[]
def isValid(i,j,n):
    if (0<=i<n and 0<=j<n):
        return True
    return False

def print_result(res):
    global ans
    d = {}
    d[0] = 'U'
    d[1] = 'D'
    d[2] = 'L'
    d[3] = 'R'
    s = []
    for i in res:
        s.append(d[i])
    ans.append(''.join(s))
    
def result(a,n,i,j):
    global visited,r,c,res
    visited[i][j] = True
    for k in range(4):
        row = i+r[k]
        col = j+c[k]
        if isValid(row,col,n) and (not visited[row][col] and a[row*n+col]):
            res.append(k)
            if row == n-1 and col == n-1:
                print_result(res)
            result(a,n,row,col)
            res.pop()
    visited[i][j] = False
            
t = int(input())
while t > 0:
    n = int(input())
    visited = [[False for i in range(n)] for j in range(n)]
    a = list(map(int,input().split()))
    (result(a,n,0,0))
    ans.sort()
    print(' '.join(ans))
    t-=1
##Sample input
##2
##4
##1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1
##4
##1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1
