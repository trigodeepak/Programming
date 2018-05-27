a = "deepak"
a = list(a)
a.sort()
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
c = []
def printUtil(s,d,a,n):
    if len(s) == n:
        c.append(''.join(s))
        return
    for i in a:
        if d[i] == 0:
            continue
        s.append(i)
        d[i]-=1
        printUtil(s,d,a,n)
        s.pop()
        d[i]+=1
printUtil([],d,a,len(a))
print c
