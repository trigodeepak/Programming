def result(a,n):
    i = 0
    b = []
    while i < 2*n:
        b.append([a[i],a[i+1]])
        i+=2
    b.sort(key = lambda x:x[0])
##    print (b)
    i = 0
    while i<n:
        if i+1<n and b[i+1][0] <= b[i][1]:
            print (b[i+1],b[i])
            b[i][1] = max(b[i][1],b[i+1][1])
            b.pop(i+1)
##            print(b)
            n-=1
            i-=1
        i+=1
    for i in b:
        print (i[0],i[1],end = ' ')
    print ()
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    result(a,n)
    t-=1
