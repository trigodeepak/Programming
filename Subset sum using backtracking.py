def check_sum(a,ind,n,s):
    if s == 0:
        return True
    if s<0:
        return False
    for i in range(ind+1,n):
        if check_sum(a,i,n,s-a[i]):
            return True
def result(a,n):
    s = (sum(a))
    if s % 2 != 0:
        print('NO')
        return 
    s = s//2
    for i in range(n):
        if check_sum(a,i,n,s-a[i]):
            print('YES')
            return
    print('NO')
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
