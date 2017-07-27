#Problem for longest palindromic subsequence
a = 'agbdba'
a = list(a)
n = len(a)
c = [[0 for i in range(n)] for x in range(n)]
for i in c:
    print i
for l in range(n):
    j = l
    i = 0
    while (j< n and i < n-l):
        print i,j
        if (i == j):
            c[i][j]=1
        elif(a[i]==a[j]):
            c[i][j] = c[i+1][j-1]+2
        else:
            c[i][j] = max(c[i+1][j],c[i][j-1])
        i+=1
        j+=1
        for x in c:
            print x
# The answer is right topmost corner , 5 in this case 
