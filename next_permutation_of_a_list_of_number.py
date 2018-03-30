def result(a,n): 
    k = n-1
    for i in range(n-2,-1,-1):
        if a[i] < a[k]:
            break
        else:
            k-=1
    ele = a[k-1]
    ind = 0
##    print (k)
    for i in range(k,n):
        if ele < a[i]:
            ind = i
    
    if k == 0:
        a = sorted(a)
        return a
    ele = a.pop(ind)
##    print (ind,ele,k,a[k])
    a = a[:k-1]+[ele]+sorted(a[k-1:])
    return a
        
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    res = (result(a,n))
    for i in res:
        print (i,end=" ")
    print ()
    t-=1
