#Program for Chocolate distribution
a = [3, 4, 1, 9, 56, 7, 9, 12]
n = 5
a.sort()
m = a[-1]
for i in xrange(len(a)-n):
    if (a[i+n-1]-a[i]<m):
        m = a[i+n-1]-a[i]
print m
