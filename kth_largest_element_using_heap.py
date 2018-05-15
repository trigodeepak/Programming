#kth largest element from a stream using min heap
def result(a,n,k):
    import heapq
    h = []
    for i in range(n):
        heapq.heappush(h,a[i])
        if k-1<i:
            (heapq.heappop(h))
        if k-1>i:
            print (-1,end = ' ')
        else:
            print (h[0],end = ' ')
##        print(h)
    print ()
t = int(input())
for _ in range(t):
    k,n = list(map(int,input().split()))
    a = list(map(int,input().split()))
    (result(a,n,k))
    
'''
1
47 84
778 916 794 336 387 493 650 422 363 28 691 60 764 927 541 427 173 737 212 369 568 430 783 531 863 124 68 136 930 803 23 59 70 168 394 457 12 43 230 374 422 920 785 538 199 325 316 371 414 527 92 981 957 874 863 171 997 282 306 926 85 328 337 506 847 730 314 858 125 896 583 546 815 368 435 365 44 751 88 809 277 179 789 585
'''
