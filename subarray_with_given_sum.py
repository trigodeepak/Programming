#sub array with the given sum
def result(a,n,m):
    i = 0
    j = 1
    s = sum(a[i:j])
    while j<n+1 :
        if s < m:
            j+=1
        elif s > m:
            i+=1
        if s == m:
            print(i+1,j)
            return 
        s = sum(a[i:j])
    print (-1)

t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    result(a,n,m)
    
