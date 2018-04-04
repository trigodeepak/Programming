#longest non repeating subarray
def result(a,n):
    d = {}
    s = 0
    e = -1
    m = 0
    i = 0
    while i<(n):
        #print (a[i],d,m,s,i)
        if a[i] not in d:
            e = i
            d[a[i]] = True
        else:
            m = max(m,e-s+1)
            i = s+1
            s = i
            e = i
            d = {}
            d[a[i]] = True
        i+=1
    m = max(m,e-s+1)
    print (m)
            
            
    
t = int(input())
while t>0:
##    n = int(input())
    a = input()
    n = len(a)
##    a = list(map(int,input().split()))
    result(a,n)
    t-=1
