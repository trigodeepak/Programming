# Partition Problem
a = [1,5,11,5]
n = len(a)
##a.sort()
s = sum(a)
b=[]
c=[]
f=0
#Now I have modified using geeksfor geeks approach
if s % 2 == 0:
    part=[[True for i in range(n+1)]for i in range(s/2+1)]
    for i in range(n):
        part[0][i]=True
    for i in range(1,s/2):
        part[i][0]=False
    for i in range(1,s/2):
        for j in range(1,n):
            part[i][j]=part[i][j-1]
            if i > a[j-1]:
                part[i][j]=part[i][j] or part[i - a[j-1]][j-1]
    f = part[s/2][n]
  
if f==False:
  print "NO"
else:
  print "YES"
