#progran for maximum sum of pairs having difference less than a value
a = [5, 15, 10, 300]
a.sort()
n = len(a)
k = 12
sum_pairs = 0
c = [0 for i in xrange(n)]
for i in xrange(1,n):
    if a[i] - a[i-1] < k:
        c[i] = c[i-2] + a[i] + a[i-1]
    else:
        c[i] = c[i-1]
    print c
print c

