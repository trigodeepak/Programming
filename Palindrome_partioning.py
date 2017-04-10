#Palindrome partitioning
n = input()
s = map(int,raw_input().strip().split(' '))
a = [1000 for i in range(n)]
b = [-1 for i in range(n)]
a[0]=0
a[1]=1
print s
for  i in range(2,n):
    for j in range(0,i-1):
        if((s[j]+j)>=i):
            print i,j
            a[i]=min(a[j]+1,a[i])
            print a
            #b[i]=j
print a
print b
# The program is not working fine but have done the logic properly
