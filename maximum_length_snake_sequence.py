#Program for maximum length of snake 
a = [[9, 6, 5, 2],[8, 7, 6, 5],[7, 3, 1, 6],[1, 1, 1, 7]]
for i in a:
	print i

c = [[1 for i in xrange(len(a[0]))]for x in xrange(len(a))]

c[0][0] = 1

for i in xrange(1,len(a[0])):
	if a[0][i-1]+1 == a[0][i] or a[0][i-1]-1 == a[0][i] :
		c[0][i] = 1 + c[0][i-1]

print "\nPrinting the solution matrix"

for i in xrange(1,len(a)):
	for j in xrange(len(a[0])):
		if j == 0:
			if a[i-1][j]+1== a[i][j] or a[i-1][j]-1 == a[i][j] :
				c[i][j] = 1+c[i-1][j]

		elif a[i-1][j]+1== a[i][j] or a[i-1][j]-1 == a[i][j]:
			if a[i][j-1]+1== a[i][j] or a[i][j-1]-1 == a[i][j]:
				c[i][j] = max(c[i-1][j]+1,c[i][j-1]+1)
			else:
				c[i][j] = (c[i-1][j]+1)
		elif a[i][j-1]+1== a[i][j] or a[i][j-1]-1 == a[i][j]:
			c[i][j] = (c[i][j-1]+1)

for i in c:
	print i
