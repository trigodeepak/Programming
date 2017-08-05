#Program for next larger element(Using Stack)
a= [13,7,6,12]
n = len(a)
c = [-1]
b = [0 for i in xrange(n)]
for i in xrange(n-1,-1,-1):
    while a[i] > c[-1] and c[-1] != -1:
        c.pop()
    b[i] = c[-1]
    c.append(a[i])
print b
#This will print the list with elements having the greatest
#number from the element at that position
