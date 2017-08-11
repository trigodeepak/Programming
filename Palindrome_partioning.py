###Palindrome partitioning
##n = input()
##s = map(int,raw_input().strip().split(' '))
##a = [1000 for i in range(n)]
##b = [-1 for i in range(n)]
##a[0]=0
##a[1]=1
##print s
##for  i in range(2,n):
##    for j in range(0,i-1):
##        if((s[j]+j)>=i):
##            print i,j
##            a[i]=min(a[j]+1,a[i])
##            print a
##            #b[i]=j
##print a
##print b
### The program is not working fine but have done the logic properly


# I don't know why it wasn't working this is a better approach palindrome partitioning
a = "abcbm"
l = len(a)
c = [[0 for i in xrange(l)]for x in xrange(l)]

#This loop is to access the matrix diagonally from left to right
for k in xrange(l):
    i = 0
    j = k
    while(i<l-k):
        if i == j:
            c[i][j] = 0
        elif (a[i] == a[j]):
            c[i][j] = 0
        else:
            min_num = c[i][0]+c[1][j]
            for x in xrange(i,j-1):
                min_num = min(min_num,c[i][x]+c[x+1][j])
            c[i][j] = 1 + min_num
        i+=1
        j+=1
for i in c:
    print i
#Program for palindrome partitioning
