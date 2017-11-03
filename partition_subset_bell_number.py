#Program for number of ways to partition a subset using bells number
a = [1]
b = [1]
n = 5
print a
for i in xrange(1,n):
	b = [a[-1]]
	for j in xrange(i):
		b.append(a[j]+b[j])
	a = list(b)
	print a
#The answer is last element of a
print "Answer is ",a[-1]
