#program to print the largest from right in a array 
a = [16, 17, 4, 3, 5, 2]
b = list(a)
n = len(a)
max_upto = a[-1]
a[-2] = a[-1]
a[-1] = -1
for i in xrange(2,n+1):
        a[-i] = max_upto
        if b[-i] > max_upto:
                max_upto = b[-i]
print a
