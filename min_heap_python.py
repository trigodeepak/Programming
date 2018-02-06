#Program for constructing a min heap than sorting the array
def min_heapify(a):
    n = len(a)
    for i in xrange(n/2,-1,-1):
        heapify(a,i,n)
    print a
    for i in xrange(n-1,-1,-1):
        t = a[0]
        a[0] = a[i]
        a[i] = t
        heapify(a,0,i)

def heapify(a,i,n):
    l = 2*i + 1
    r = 2*i + 2
    smallest = i
    if (l<n and a[l]<a[smallest]):
        smallest = l
    if (r<n and a[r]<a[smallest]):
        smallest = r
    if smallest != i:
        t = a[i]
        a[i] = a[smallest]
        a[smallest] = t
        heapify(a,smallest,n)

a = [12, 11, 13, 5, 6, 7]
min_heapify(a)
print a   
