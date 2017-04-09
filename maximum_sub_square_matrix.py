#Program for maximum Sub square matirix using dp
##n = input()
##m = input()
##a = [[] for i in range(n)]
##for i in range(n):
##  for j in range(m):
##    b = input()
##    a[i].append(b)
n=5
m=4
a = [[0,0,1,1,1],
     [1,0,1,1,1],
     [0,1,1,1,1],
     [1,0,1,1,1]]
print a
c=[[0 for j in range(m)] for i in range(n)]
for i in range(n):
  for j in range(m):
    if(i==0 or j==0):
      c[i][j]=0
    else:
      c[i][j]= 1+ min(c[i-1][j],c[i-1][j-1],c[i][j-1])
for i in range(n):
  print c[i]
#Taking input is not working fine becaue taking input for matrix
