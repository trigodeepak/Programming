#python code for reversing words in a string
a = "i.like.this.program.very.much"
a = a.split('.')
l = len(a)
b = []
for i in xrange(l-1,-1,-1):
    b.append(a[i]+'.')
print ''.join(b)
