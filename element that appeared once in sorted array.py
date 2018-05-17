#Element that appeared once in sorted array
def result(a,n):
    for i in range(0,n-1,2):
        if a[i]!= a[i+1]:
            print (a[i])
            return 

    print (a[n-1])
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))
    
'''Sample input
1
11
1 1 2 2 3 3 4 50 50 65 65
'''
