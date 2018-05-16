def result(a,n):
    current = 0
    max_sum = 0
    for i in range(n):
        current+=a[i]
        max_sum = max(current,max_sum)
        if current<0:
            current = 0
    #To handle negative elements
    if max(a) < 0:
        print (max(a))
        return
    print(max_sum)
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result(a,n)
'''Sample input
2
3
1 2 3
4
-1 -2 -3 -4
'''
