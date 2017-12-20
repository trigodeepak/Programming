##minimum cost to make two strings identical
x = list("ef")
y = list("gh")
costx = 10
costy = 20
def find_lcs(x,y):
   n = len(x)
   m = len(y)
   c = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
   for i in xrange(n+1):
      for j in xrange(m+1):
         if i == 0 or j == 0:
            continue
         if x[i-1] == y[j-1]:
            c[i][j] = c[i-1][j-1] + 1
         else:
            c[i][j] = max(c[i-1][j],c[i][j-1])
   return c[n][m]
l = find_lcs(x,y)
print (len(x)-l)*costx+(len(y)-l)*costy
