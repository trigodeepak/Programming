s = "ababd"
n = len(s)
if n ==1:
    print s[0]
c = [[False for i in xrange(n)] for j in xrange(n)]
maxlen = [0,0,0]
for i in xrange(n-1):
    c[i][i] = True
    if s[i] == s[i+1]:
        c[i][i+1] = True
        if 1 > maxlen[0]:
            maxlen = [1,i,i+2]
c[i+1][i+1] = True
for l in xrange(3,n+1):
    i = 0
    j = l-1
    while(j<n):
        if s[i] == s[j]:
            c[i][j] = True and c[i+1][j-1]
            if c[i][j] and j-i+1 > maxlen[0]:
                maxlen = [j-i+1,i,j+1]
        i+=1
        j+=1
for i in c:
    print i  
print s[maxlen[1]:maxlen[2]]
