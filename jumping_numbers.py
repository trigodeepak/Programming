#Program for jumping numbers i.e. Numbers which have
#exactly 1 difference between their digits
a = 100
d = [i for i in xrange(10)]
l = len(d)
i = 1
def increase(x):
    x += 1
    if x>9:
        x = 0
    return x
def decrease(x):
    x -= 1
    if x<0:
        x = 9
    return x

while(i<l):
    if ((d[i]*10+increase(d[i]%10)) <= a):
        d.append(d[i]*10+increase(d[i]))
        l+=1
##        print d[-1]
    if ((d[i]*10+decrease(d[i]%10))<= a):
        d.append(d[i]*10+decrease(d[i]))
        l+=1
##        print d[-1]
    i+=1

print d
