#sumuptolargeno_usingshiftOperators.py
a = raw_input().strip()
#print a
a = int(a,2)
print a
b = raw_input().strip()
#print b,type(b)
b = int(b,2)
print b<<2
s=0
for i in range(314159):
    s+=a^(b<<(i))
print s%(10**9+7)
#Done in python for large numbers but they say large numbers not needed, output is not correct after using python though
