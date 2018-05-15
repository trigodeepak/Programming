#Leaders in an array
def result(a,n):
    m = a[n-1]
    b = []
    b.append(m)
    for i in range(n-2,-1,-1):
        if a[i] > m:
            m = a[i]
            b.append(m)
    print(' '.join([str(i) for i in b[::-1]]))
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
    
