#minimum jumps to reach end
n = input()
s = map(int,raw_input().strip().split(' '))
a = [1000 for i in range(n)]
b = [-1 for i in range(n)]
a[0]=0
print s
for  i in range(1,n):
    for j in range(0,i):
        if((s[j]+j)>=i):
            print i,j
            a[i]=min(a[j]+1,a[i])
            print a
            #b[i]=j
print a
print b
#Output is coming now
#Try this, this works totally fine

###Program for mininmum number of jumps to reach the end
##a = [2,3,1,1,2,4,2,0,1,1]
##n = len(a)
##c = [9999 for i in xrange(n)]
##c[0] = 0
##for i in xrange(n):
##    for j in xrange(i):
##        if(i<=a[j]+j):
##            c[i]=min(c[i],c[j]+1)
##print c
### The answer is 4 in this case 

