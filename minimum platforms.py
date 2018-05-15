#Minimum platforms
def result(n,s,d):
    s = list(zip(s,['s']*n))
    d = list(zip(d,['d']*n))
    for i in range(n):
        if s[i][0]>d[i][0]:
            d[i]=(2400+d[i][0],'d')
    d.sort(key= lambda x :x[0])
    s.sort(key= lambda x :x[0])
    itr1 = 0
    itr2 = 0
    count = 0
    m  = 0
    #this is done similar to the merging of two arrays using smaller element and increasing the count
    while(itr1<n and itr2<n):
        if s[itr1]<d[itr2]:
            count+=1
            itr1+=1
            m = max(count,m)
        else:
            count-=1
            itr2+=1
    print(m)
    
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    d = list(map(int,input().split()))
    (result(n,s,d))
