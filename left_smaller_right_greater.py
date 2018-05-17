#left smaller right greater
def result(a,n):
    left = []
    left.append(a[0])
    right = []
    right.append(a[-1])
    n = len(a)
    for i in range(1,n):
        if(left[i-1]<a[i]):
            left.append(a[i])
        else:
            left.append(left[i-1])
        if(right[i-1]>a[n-1-i]):
            right.append(a[n-1-i])
        else:
            right.append(right[i-1])
    #reversing the right array
    right = right[::-1]
    for i in range(1,n-1):
        if left[i] == right[i]:
            print (left[i])
            return
    print (-1)
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n))

'''Sample Input
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9
'''
