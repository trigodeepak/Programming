#Program to make all element of rows and columns containing 1
##equal to 1
def result(a,n,m):
    row = []
    col = []
    for i in range(n):
        for j in range(m):
            if a[i*m+j] == 1:
                row.append(i)
                col.append(j)
    row = list(set(row))
    col = list(set(col))
    for i in row:
        for j in range(m):
            a[i*m+j] = 1
    for i in range(n):
        for j in col:
            a[i*m+j] = 1
    print (' '.join([str(i) for i in a]))
        
t = int(input())
while t > 0:
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    (result(a,n,m))
    
    t-=1
