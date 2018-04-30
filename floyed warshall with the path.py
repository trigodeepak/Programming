#Program for floyd warshall with the path of vertices
n,m = list(map(int,input().split()))
graph = [[float('inf') for i in range(n)] for j in range(n)]
path = [[False for i in range(n)] for j in range(n)]
for i in range(n-1):
    a = list(map(int,input().split()))
    graph[a[0]-1][a[1]-1] = 1
    graph[a[1]-1][a[0]-1] = 1
    path[a[0]-1][a[1]-1] = a[0]-1
    path[a[1]-1][a[0]-1] = a[1]-1
calc = []
for i in range(m):
    calc.append(list(map(int,input().split())))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[k][j]
##for i in graph:
##    print(i)
##print('Printing path')
##for i in path:
##    print(i)

from collections import defaultdict
d = defaultdict(int)

for k in calc:
    ver = path[k[0]-1][k[1]-1]
    d[k[1]-1]+=1
    while (ver != k[0]-1):
        d[ver]+=1
        ver = path[k[0]-1][ver]
    d[ver]+=1

print (max(d.values()))
#sample input
inp = '''
4 2
1 2
2 3
2 4
1 4
3 4
'''
