#Sort according to other list
a = [[] for i in xrange(2)]
a[0] = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a[1] = [2, 1, 8, 3]
d = {}
for i in xrange(len(a[1])):
    d[a[1][i]] = i


b = []
i = 0
while i <(len(a[0])):
    if a[0][i] not in d:
        b.append(a[0][i])
        a[0].pop(i)
        i-=1
    i+=1
    
n = len(a[0])
for i in xrange(n):
    for j in xrange(n-i-1):
        if d[a[0][j]]>d[a[0][j+1]]:
            t = a[0][j]
            a[0][j] = a[0][j+1]
            a[0][j+1] = t
print a[0]+b
            
