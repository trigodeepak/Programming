#Count number of ways to reach destination in a Maze
a = [[0,  0, 0, 0],
     [0, -1, 0, 0],
     [-1, 0, 0, 0],
     [0, 0, 0, 0]]
r = 4
c = 4

c = [[0 for i in range(4)]for j in range(4)]
c[0][0] = 1

for i in range(4):
    for j in range(4):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            if a[i][j] != -1:
                c[i][j] = c[i][j-1]
        elif j == 0:
            if a[i][j] != -1:
                c[i][j] = c[i-1][j]
        elif a[i][j] != -1:
            c[i][j]+=c[i-1][j]+c[i][j-1]
        

for i in c:
    print i
    
