#Replace 'O' with 'X' in a given matrix
def is_safe(i,j,n,m):
    if 0<=i<n and 0<=j<m:
        return True
    return False

def floodfill(a,n,m,i,j,ch1,ch2):
    if a[i*m+j] == ch1:
        a[i*m+j] = ch2
    for k in range(4):
        r = i+row[k]
        c = j+col[k]
        if is_safe(r,c,n,m) and a[r*m+c]==ch1:
            floodfill(a,n,m,r,c,ch1,ch2)
            
def result(a,n,m):
    #Applying flood fill 2 times
    for i in range(n):
        for j in range(m):
            if i == n-1 or i == 0 or j == 0 or j == m-1:
                if a[i*m+j] == 'i':
##                    print (i,j,a[i*m+j])
                    floodfill(a,n,m,i,j,'i','O')
    for i in range(n):
        for j in range(m):
            if a[i*m+j] == 'i':
                floodfill(a,n,m,i,j,'i','X')
            
        
row = [1,-1,0,0]
col = [0,0,1,-1]

t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = input().strip().split()
##    for i in range(n):
##        print (a[i*m:(i+1)*m])
    for i in range(n):
        for j in range(m):
            if a[i*m+j]!='X':
                a[i*m+j] = 'i'
    result(a,n,m)
    print(' '.join(a))
##    for i in range(n):
##        print (a[i*m:(i+1)*m])
