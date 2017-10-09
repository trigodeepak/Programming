#Program to recursively remove all the same arrays
a = 'geeksforgeeg'
a = list(a)
l = len(a)
i = 0

while(i<l-1):
    if a[i] == a[i+1]:
        s = i
        a.pop(i+1)
        l-=1
        while(i+1<l and a[i]==a[i+1]):
            a.pop(i+1)
            l-=1
        a.pop(i)
        l-=1
        i-=2
    i+=1
print ''.join(a)

