#Word boggle using dfs of graph mainly it is backtracking
# Generating all the sequences of the character available
def is_safe(i,j,n,m):
    if 0<=i<n and 0<=j<m:
        return True
    return False

def dfsUtil(a,n,m,d,i,j,s):
    global visited,res
##    print (s,i,j)
    if s in d:
        res.append(s)
        d.pop(s)
    if len(d) == 0 or len(s)>len(max(d.keys())) :
        return 
    
    for k in range(8):
        r = i+row[k]
        c = j+col[k]
        if is_safe(r,c,n,m) and not visited[r][c]:
            visited[r][c] = True
            dfsUtil(a,n,m,d,r,c,s+a[r*m+c])
            visited[r][c] = False

def result(a,n,m,d):
    global visited
    for i in range(n):
        for j in range(m):
            visited = [[False for i in range(m)]for j in range(n)]
            dfsUtil(a,n,m,d,i,j,'')

row = [-1,-1,-1,0,0,1,1,1]
col = [-1,0,1,-1,1,-1,0,1]

visited = [[]]
res = []
t = int(input())
for _ in range(t):
    n = int(input())
    d = input().split()
    #creating a dictionary of the words
    temp = {}
    for i in d:
        temp[i] = True
    d = temp
    n,m = list(map(int,input().split()))
    a = input().split()
    result(a,n,m,d)
    if res == []:
        print (-1)
    else:
        print (' '.join(sorted(res)))
    res = []
    
'''Sample input
1
4
GEEKS FOR QUIZ GO
3 3
G I Z U E K Q S E
'''
