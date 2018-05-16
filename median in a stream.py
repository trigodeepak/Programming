#Median in a stream using 2 heaps 
def rebalance(h_min,h_max,l1,l2):
    if l1>l2:
        heapq.heappush(h_max,-heapq.heappop(h_min))
        l1-=1;l2+=1
    else:
        heapq.heappush(h_min,-heapq.heappop(h_max))
        l2-=1;l1+=1
    return l1,l2

import heapq
h_min = []
h_max = []
l1 = 0
l2 = 0
med = 0

t = int(input())
for i in range(t):
    n = int(input())
    if l1 == 0 or n<=med:
        heapq.heappush(h_min,-n)
        l1+=1
    elif n>med:
        heapq.heappush(h_max,n)
        l2+=1
    if abs(l1-l2) >= 2:
        l1,l2 = rebalance(h_min,h_max,l1,l2)
        
    #finding median and printing
    if l1>l2:
        med = -h_min[0]
    elif l1<l2:
        med = h_max[0]
    else:
        med = ((-h_min[0]+h_max[0])/2.0) 
    print (med)
    
