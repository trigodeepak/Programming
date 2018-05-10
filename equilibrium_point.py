#Equililbrium point
def result(a,n):
    s = sum(a)
    left_s = 0
    for i in range(n):
        s-=a[i]
        if left_s == s:
            print (a[i])
            return 
        left_s += a[i]
    print (-1)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result(a,n)
    
