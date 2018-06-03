#Job scheduling with a deadline
def result(a,n):
    count = 0
    profit = 0
    a.sort(key = lambda x:x[1],reverse = True)
    #visited dictionary for greatest time slot
    visited = {}
    for i in range(n):
        j = a[i][0]
        while (j>0 and j in visited):
            j-=1
        if j!=0:
            count+=1
            profit+=a[i][1]
            visited[j] = True
##        print(count,profit,visited)
    print(count,profit)
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i*3+1:(i*3)+3])
    a = b
    (result(a,n))
