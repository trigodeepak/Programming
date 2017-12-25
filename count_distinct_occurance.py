#Count distinct occurance as a subsequence
s = "banana"
t = "ban"
def subsequences(s,t,n,m):
    c = [[0 for i in xrange(m+1)]for j in xrange(n+1)]
    for i in xrange(n+1):
        for j in xrange(m+1):
            if j == 0:
                c[i][j] = 1
            elif i == 0:
                c[i][j] = 0
            elif s[i-1] == t[j-1]:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
            else:
                c[i][j] = c[i-1][j]
##    for i in c:
##        print i
    return c[n][m]
##    if m == 0:
##        return 1
##    if n == 0:
##        return 0
##    if s[n-1] == t[m-1]:
##        return subsequences(s,t,n-1,m-1)+subsequences(s,t,n-1,m)
##    else:
##        return subsequences(s,t,n-1,m)
n = len(s)
m = len(t)
print subsequences(s,t,n,m)
