import heapq
def result(h,n):
    res = []
    while len(h)>1:
        i = heapq.heappop(h)
        j = heapq.heappop(h)
        res+=[i,j]
        heapq.heappush(h,(i[0]+j[0],'internal node'))
    res.append(h[0])
    print (res)
        
t = int(input())
for _ in range(t):
    a = list(input().strip())
    n = len(a)
    freq = list(map(int,input().split()))
    h = []
    for i in range(n):
        h.append((freq[i],a[i]))
    heapq.heapify(h)
    (result(h,n))
