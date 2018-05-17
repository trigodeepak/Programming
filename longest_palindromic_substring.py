def result(s,n):
    n = len(s)
    if n == 1:
        print (s[0])
        return 
    c = [[False for i in range(n)] for j in range(n)]
    maxlen = [0,0,0]
    for i in range(n-1):
        c[i][i] = True
        if s[i] == s[i+1]:
            c[i][i+1] = True
            if 1 > maxlen[0]:
                maxlen = [1,i,i+2]
    c[i+1][i+1] = True
    for l in range(3,n+1):
        i = 0
        j = l-1
        while(j<n):
            if s[i] == s[j]:
                c[i][j] = True and c[i+1][j-1]
                if c[i][j] and j-i+1 > maxlen[0]:
                    maxlen = [j-i+1,i,j+1]
            i+=1
            j+=1
    for i in c:
        print (i)
    if maxlen[1]==maxlen[2]:
        print (s[0])
        return
    print (s[maxlen[1]:maxlen[2]])

t = int(input())
for _ in range(t):
    a = input()
    n = len(a)
    (result(a,n))
