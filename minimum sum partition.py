#minimum sum partition
#do it using knapsack next time
def check_sum(a,ind,n,s,a_s):
    global m
    if m == a_s//2 or s>a_s//2:
        return
    else:
        m = max(s,m)
        if m == a_s//2:
            return 
    for i in range(ind+1,n):
        check_sum(a,i,n,s+a[i],a_s)

def result(a,n):
    s = (sum(a))
    for i in range(n):
        check_sum(a,i,n,a[i],s)
    print(abs(s-m-m))
m = 0
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
