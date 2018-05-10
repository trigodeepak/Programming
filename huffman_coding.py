import heapq
def result(h,n):
    res = []
    while len(h)>1:
        i = heapq.heappop(h)
        j = heapq.heappop(h)
        heapq.heappush(h,[i[0]+j[0],'internal node',i,j])
    #the h[0] node will contain the whole tree
    traverse_tree(h[0],[])
    print()
    
def traverse_tree(node,sym):
    #length less than 3 means the node is a leaf node
    if len(node)<3:
##        print(node,sym)
        print(''.join([str(i) for i in sym]),end=' ')
        return
    traverse_tree(node[2],sym+[0])
    traverse_tree(node[3],sym+[1])

t = int(input())
for _ in range(t):
    a = list(input().strip())
    n = len(a)
    freq = list(map(int,input().split()))
    h = []
    #We can build a heap of list and it will heapify them according to the first or 0th index
    #heapify only does min heap
    for i in range(n):
        h.append([freq[i],a[i]])
    heapq.heapify(h)
##    print(h)
    (result(h,n))
