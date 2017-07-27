a = 'abcdef'
a = list(a)
b = 'azced'
b = list(b)
## Minimum operations to convert from one place to other
c = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
for i in range(len(b)+1):
    for j in range(len(a)+1):
##        print i,j
##        print b[i-1]
        if(i==0):
            c[i][j]= j
        elif(j==0):
            c[i][j]= i
        elif(a[j-1]==b[i-1]):
            c[i][j] = c[i-1][j-1]
        else:    
            c[i][j]=min(c[i-1][j-1],c[i][j-1],c[i-1][j])+1
for i in c:
    print i
# the last value is the answer 3 in this case
