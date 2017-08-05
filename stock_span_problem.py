#Program for stock span problem
a= [100,80,60,70,60,75,85]
n = len(a)
max_till = 1
c = [1 for i in xrange(n)]
for i in xrange(n):
    for j in xrange(i):
        if(a[i]>a[j]):
            max_till += 1
        else:
            max_till = 1
    c[i] = max_till
print c
# The answer is an array showing max span for each stock day.
# Now for the more optimum solution
c = [1 for i in xrange(n)]
for i in xrange(n):
    for j in xrange(i-1,-1,-1):
        if(a[i]<a[j]):
            c[i] = i-j
            break        
print c

