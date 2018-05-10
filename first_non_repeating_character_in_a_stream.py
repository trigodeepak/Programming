#first non repeating character in a stream
def result(a,n):
##    print(a,n)
    from collections import defaultdict
    d = defaultdict(int)
    f = [-1]
    d[-1] = 1
    for i in a:
        d[i] += 1
        while d[f[-1]] > 1:
            f.pop()
        if d[i] == 1:
            f.insert(1,i)
        print (f)
        print(f[-1],end = ' ')
    print()
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().split())
    result(a,n)
    
