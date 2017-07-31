#Program to know the coin changing subproblem
a = [7,2,3,6]
n = 13
c = [float('inf') for i in xrange(n+1)]
c[0] = 0
d = [-1 for i in xrange(n+1)]
print c
for i in xrange(len(a)):
    for j in xrange(n+1):
        if(j>=a[i]):
            c[j] = min(c[j],1+c[j-a[i]])
print c
#Now I know how to debug a python program
# the answer is 2
