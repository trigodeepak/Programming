#Program for stepping numbers using bfs method
def bfs(n,m,i):
    global res
##    print ('the function call is for ',m,n,i)
    q = [i]
    while len(q) > 0:
##        print (q,res)
        stepnum = q.pop(0)
        if n<=stepnum<=m:
            res.append(stepnum)
        if i == 0 or stepnum > m:
            continue
        l = stepnum%10
        a = stepnum*10 + l+1
        b = stepnum*10 + l-1
        if l == 0:
            q.append(a)
        elif l == 9:
            q.append(b)
        else:
            q+=[a,b]
        
def result(n,m):
    for i in range(10):
        (bfs(n,m,i))
         
res = []
t = int(input())
while t > 0:
    res = []
    n,m = list(map(int,input().split()))
    result(n,m)
    print (len(res))
    t-=1
