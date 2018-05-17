#convert into zig-zag
def swap(a,b):
    return b,a
def result(a,n):
    for i in range(n-1):
        if i % 2 == 0:
            if a[i] > a[i+1]:
                a[i],a[i+1] = swap(a[i],a[i+1])
        else:
            if a[i] < a[i+1]:
                a[i],a[i+1] = swap(a[i],a[i+1])
    print (' '.join([str(i) for i in a]))
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
    
'''Sample input
2
7
4 3 7 8 6 2 1
4
1 4 3 2
'''
