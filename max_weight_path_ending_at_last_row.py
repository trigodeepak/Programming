#progran for Maximum weight path ending at any element of last row in a matrix
a = [[ 4, 2 ,3 ,4 ,1 ],
 [ 2 , 9 ,1 ,10 ,5 ],
 [15, 1 ,3 , 0 ,20 ],
 [16 ,92, 41, 44 ,1],
 [8, 142, 6, 4, 8] ]
n = len(a)
m = len(a[0])
c = [[0 for i in xrange(m)]for x in xrange(n)]
c[0][0] = a[0][0]
for i in xrange(1,n):
	for j in xrange(i):
		if j == 0:
			c[i][j] =	a[i][j] + c[i-1][j]
		else:
			c[i][j] = a[i][j] + max(c[i-1][j-1],c[i-1][j])
for i in c:
	print i
#answer is 255 in this case
