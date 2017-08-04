#Program for maximum sum increasing subsequence
a= [4,6,1,3,8,4,6]
n = len(a)
c = [i for i in a]
for i in xrange(n):
    for j in xrange(i):
        if(a[i]>a[j]):
            c[i]=max(c[i],c[j]+a[i])
print c
# The answer is 18 in this case which is max in this array.
