#shortes common supersequence
a = "aggtab"
b = "gxtxayb"
n = len(a)
m = len(b)
c = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
for i in xrange(n+1):
    for j in xrange(m+1):
        if i == 0 or j == 0:
            continue
        elif a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i-1][j],c[i][j-1])
print "And the answer is ",n+m-c[n][m]
