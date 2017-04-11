# Partition Problem
a = [1,5,11,5]
n = len(a)
a.sort()
s = sum(a)
b=[]
c=[]
f=0
#This algorithm does that it makes two list from beginning and end and keep
#on comparing their sum if same and we have traversed the whole array then
#The output will be yes in all other cases the output will be no.
for i in range(n):
  if s % 2 != 0:
    f = 0
    break
  k = 0
  c.append(a[k])
  j = n-1
  b.append(a[j])
  f=1
  while sum(b)!=sum(c) and (j + k <= n):
    if(sum(b)<sum(c)):
      b.append(a[j-1])
      j-=1
      print b
    else:
      c.append(a[k+1])
      k+=1
      print c
    if(k>=j):
      f=0
      break
if f==0:
  print "NO"
else:
  print "YES"
#At last it worked for the sample test case ; )
