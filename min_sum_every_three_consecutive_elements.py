#minimum sum one every three consecutive elements
a = [1, 2, 3, 6, 7, 1, 8, 6, 2, 7, 7, 1]
n = len(a)
s = [0 for i in xrange(n)]
print a
s[0] = a[0]
s[1] = a[1]
s[2] = a[2]
for i in xrange(3,n):
    s[i] = a[i] + min(s[i-1],s[i-2],s[i-3])
print s
print "Answer is : ",min(s[n-1],s[n-2],s[n-3])
