#Program for the smallest window
##a = 'abmmebezedeedzbfjfazdjdje'
##a = list(a)
##l = len(a)
##b = 'ebdz'
##b = list(b)
##n = len(b)

#For paragraph input 
a = raw_input().split(' ')
l = len(a)
n = input()
b = []
for i in xrange(n):
    d = raw_input().strip()
    b.append(d)

#C is count dictionary
c = {}
for i in xrange(n):
    c[b[i]] = 0
count = 0
window = float('inf')
for i in xrange(l):
    if (a[i] in b):
        char = a[i]
        if(c[a[i]]== 0 ):
            count+=1
        c[a[i]] = i
        if count == n:
            val = max(c.values())-min(c.values())
            if window > val:
                window = val
#To print the window size
print window + 1
mini = min(c.values())
maxi = max(c.values())
for i in xrange(mini,maxi+1):
    print a[i],
    
