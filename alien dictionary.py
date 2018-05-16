#Alien dictionary
from collections import defaultdict
def result(a,n,m):
    global visited,d
    d = defaultdict(list)
    for i in range(n-1):
        for j in range(min([len(a[i]),len(a[i+1])])):
            if a[i][j] != a[i+1][j]:
                d[a[i][j]].append(a[i+1][j])
                if a[i+1][j] not in d:
                    d[a[i+1][j]] = []
                break
    print(d)
    #Applying dfs
    for i in d:
        visited[i] = False
    sol = []
    for i in d:
        if not visited[i]:
            sol += dfs(i)
    #Apply topological sort
    return (''.join(sol))

def dfs(q):
    #Function for dfs
    sol = []
    stack = []
    visited[q]=True
    while True:
        sol.append(q)
        for j in d[q]:
            if not visited[j]:
                stack.append(j)
                visited[j]=True
        if len(stack)==0:
            break
        q = stack.pop()
    return s
    
visited = {}
d = {}
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = input().split()
    print(result(a,n,m))
