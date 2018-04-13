#Program for Unique bsts formed using Catalan number 
def result(n,k):
    import math
    f = math.factorial
    print (int(f(n)/f(n-k)/f(k)/(k+1)))

t = int(input())
while t > 0:
    n = int(input())
##    n,m = list(map(int,input().split()))
    result(2*n,n)

    t-=1
