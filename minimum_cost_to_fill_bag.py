#program to print the minimum cost to fill a bag 
# it is not working correctly
a = [20, 10, 4, 50, 100]
n = len(a)
wt = []
v = []
for i in xrange(n):
	if a[i]!=-1:
		wt.append(i+1)
		v.append(a[i])
print wt
n = len(v)
w = 5
c = [[0 for i in xrange(n+1)]for j in xrange(w+1)]
for i in xrange(w+1):
	for j in xrange(n+1):
		if i == 0 or j == 0:
			c[i][j] = 99999
		elif wt[i-1] > j:
			c[i][j] = c[i-1][j]
		elif wt[i-1] >= j:
			c[i][j] = min(c[i-1][j],v[i-1]+c[i][j-wt[i-1]])
for i in c:
	print i
