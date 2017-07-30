#Program to find longest common subsequence from two strings
a = "abcdef"
a = list(a)
b = "acbcf"
b = list(b)
n = len(a)+1
m = len(b)+1
c = [[0 for i in range(n)]for x in range(m)]
for i in range(m):
    for j in range(n):
##        print j,b[i]
        if(i==0 or j==0):
            c[i][j]= 0
        elif(a[j-1]==b[i-1]):
            c[i][j] = c[i-1][j-1]+1
        else:
            c[i][j] = max(c[i-1][j],c[i][j-1])
for i in c:
    print i
# The last digit is the answer to the problem
