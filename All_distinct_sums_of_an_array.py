#Find all distinct subset (or subsequence) sums of an array
a = [1, 2, 3]
d = []
d = [0]
def count_sums(a,n,d):
    b = []
    for i in a:
        for j in d:
            b.append(i+j)
        d = d + b
        d = set(d)
        d = list(d)
        d.sort()
        print d
    return d

def count_sums_dp(a,n):
    s = sum(a)
    c = [[False for i in xrange(s+1)] for j in xrange(n+1)]
    for i in xrange(n+1):
        c[i][0] = True

    for i in xrange(1,n+1):
        c[i][a[i-1]] = True
        for j in xrange(s+1):
            if c[i-1][j] == True:
                c[i][j] = True
                c[i][j+a[i-1]] = True
    for j in xrange(s+1):
        if c[n][j] == True:
            print j,
    
    for i in c:
        print i
    
n = len(a)
##print count_sums(a,n,d)
count_sums_dp(a,n)
