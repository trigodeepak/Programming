#Program for longest increasing subsequence
a = [3,4,-1,0,6,2,3]
n = len(a)
c = [1 for i in xrange(n)]
for i in xrange(n):
    for j in xrange(i):
        if a[j] < a[i] :
            c[i] = max (c[i],c[j]+1)
print c
# The answer is 4 in this case
        
