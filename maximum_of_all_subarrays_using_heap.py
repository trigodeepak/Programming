#maximum of all subarrays of size k
def result(a,n,k):
    import heapq
    h = []  
    for i in range(n):
        heapq.heappush(h,-a[i])
        if i>k-1:
            h.remove(-a[i-k])
            heapq.heapify(h)
        if i >= k-1:
            print (-h[0],end=' ')
    print ()    
t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    (result(a,n,k))
