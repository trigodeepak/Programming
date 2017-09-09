#Program to transform one string to another if only
#taking one character and putting it into front is
#allowed
a = list("ABD")
b = list("BAD")
m = len(a)
n = len(b)
s = 1
f = 0
if m == n:
    for i in xrange(m-1, -1, -1):
        if a[i] == b[i]:
            a.pop()
            b.pop()
            continue
        else:
            if b[i] in a:
                s+=a.index(b[i])
                a.pop(a.index(b[i]))
            else:
                f = 1
else:
    f = 1
if f == 0:
    print s

