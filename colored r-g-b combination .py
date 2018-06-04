#https://www.geeksforgeeks.org/count-number-of-strings-made-of-r-g-and-b-using-given-combination/
def result(n,r,g,b):
    fact = [1]*(n+1)
    fact[0] = 1
    for i in range(1,n+1):
        fact[i] = i*fact[i-1]
    left = n-(r+b+g)
    s = 0
    for i in range(left+1):
        for j in range(left-i+1):
            k = left-(i+j)
            s+=fact[n]//(fact[i+r]*fact[j+g]*fact[b+k])
    print(s)
t = int(input())
for _ in range(t):
    n,r,g,b = list(map(int,input().split()))
    (result(n,r,g,b))
