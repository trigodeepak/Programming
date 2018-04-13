#Program for rainwater trapping    
def result(a,n):
    l = [0]*n
    r = [0]*n
##    print(a)
    m = a[0]
    l[0] = m
    for i in range(n-1):
        m = max(m,a[i+1])
        l[i+1] = m
    m = a[-1]
    r[-1] = m
    for i in range(n-1,0,-1):
        m = max(m,a[i-1])
        r[i-1] = m
    res = 0
    for i in range(n):
        res+= min(l[i],r[i])-a[i]
    print (res)
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    result(a,n)
    t-=1
