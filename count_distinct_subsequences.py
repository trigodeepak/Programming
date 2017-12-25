#Count distinct subsequences
s = "gfg"
n = len(s)
c = [0]*(n+1)
d = {}
c[0] = 1
for i in xrange(1,n+1):
    c[i] = 2*c[i-1]
    if s[i-1] in d:
        c[i] -= c[d[s[i-1]]]
    d[s[i-1]] = i-1
print c
#Answer is c[n]
print c[n]
