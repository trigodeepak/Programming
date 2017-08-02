#Program to find longest common substring(just the string is continuous)
a = "abcdef"
a = list(a)
b = "acbcf"
b = list(b)
n = len(a)+1
m = len(b)+1
c = [[0 for i in range(n)]for x in range(m)]
for i in range(m):
    for j in range(n):
        if(i==0 or j==0):
            c[i][j]= 0
        elif(a[j-1]==b[i-1]):
            c[i][j] = c[i-1][j-1]+1
        else:
            c[i][j] = 0
for i in c:
    print i
#Iterate and find the biggest number and
    #this is the max common substring 2 in this case
