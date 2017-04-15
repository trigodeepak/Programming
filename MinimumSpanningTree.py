#Minimum spanning tree using prims algorithm
graph = [[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]
n = 5
for i in range(n):
    for j in range(n):
        if (graph[i][j]==0):
            graph[i][j]= 9999

ini = 0
color = []
for i in range(n):
    color.append(0)
i=0
print i
while True:
    color[i]=1
    ind = graph[i].index(min(graph[i]))
    while (color[ind]==1):
        graph[i][ind]=9999
        ind = graph[i].index(min(graph[i]))
    print ind
    color[ind] = 1
    i = ind
    if 0 not in color:
        break
