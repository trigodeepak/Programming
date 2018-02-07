#Program for the biggest number for array
a = "54 546 548 60"
a = a.split()
b = [a[0]]

for i in xrange(1,len(a)):
    m = int(a[i]+''.join(b))
    ind = 0
    for j in xrange(i):
        if m<int(''.join(b[:j])+a[i]+''.join(b[j:])):
            ind = j
    b.insert(ind,a[i])
print ''.join(b)
        
