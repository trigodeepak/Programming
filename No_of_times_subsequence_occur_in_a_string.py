#find number of times a subsequence occur in a string
x = list('Gks')
y = list('GeeksforGeeks')
n = len(x)
m = len(y)
c = [[0 for i in xrange(n+1)]for j in xrange(m+1)]

for i in xrange(m+1):
   c[i][0] = 1

for i in xrange(1,m+1):
   for j in xrange(1,n+1):
      if x[j-1]== y[i-1]:
         c[i][j] = c[i-1][j-1] + c[i-1][j]
      else:
         c[i][j] = c[i-1][j]

for i in c:
   print i
   
