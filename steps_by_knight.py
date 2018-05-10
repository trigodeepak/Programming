def is_safe(i,j,n):
    if 0<=i<n and 0<=j<n:
        return True
    return False

def result(s,t,n):
    global visited,row,col,res
    q = [s+[0]]
    itr = -1
    while True:
        l = len(q)
        itr+=1
        for i in range(l):
            node = q.pop(0)
            for k in range(8):
                r = node[0]+row[k]
                c = node[1]+col[k]
                if is_safe(r,c,n) and not visited[r][c]:
                    visited[r][c] = True
                    if t==[r,c]:
                        print (node[2]+1)
                        return
                    q.append([r,c,itr])
            
row = [-2,-2,2,2,-1,1,-1,1]
col = [-1,1,-1,1,-2,-2,2,2]
visited = []
t = int(input())
for _ in range(t):
    n = int(input())
    visited = [[False for i in range(n)]for j in range(n)]
    start = list(map(int,input().split()))
    target = list(map(int,input().split()))
    start = [start[0]-1,start[1]-1]
    target = [target[0]-1,target[1]-1]
    (result(start,target,n))
