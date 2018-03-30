r = [-1,-1,-1,0,0,1,1,1]
c = [-1,0,1,-1,1,-1,0,1]
def is_valid(r,c,n,m):
    if (0<=r<n and 0<=c<m):
        return True
    return False
def dfs(a,i,j,visited,n,m):
    visited[i][j] = True
##    print (i,j)
##    for p in visited:
##        print (p)
    for k in range(8):
        row=i+r[k]
        col=j+c[k]
##        print (row,col)
        if is_valid(row,col,n,m) and not visited[row][col] and a[row][col]:
##            print ('dfs called',row,col)
            visited = dfs(a,row,col,visited,n,m)
##    print ()
    return visited
            
a = [[1, 1, 0], [0, 0, 1], [1, 0, 1]]
visited = [[False for i in range(3)] for i in range(3)]
count = 0
for i in range(3):
    for j in range(3):
        if not visited[i][j] and a[i][j]:
            count+=1
            visited = dfs(a,i,j,visited,3,3)
print (count)
