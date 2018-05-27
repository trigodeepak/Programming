#Smallest element on left side
def result(a,n):
    s = [-1]
    for i in range(n):
        # print(s)
        while (s[-1]>=a[i]):
                s.pop()
        print(s[-1],end=' ')
        s.append(a[i])
    print()
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
