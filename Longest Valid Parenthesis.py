#Longest valid Parenthesis
def result(a,n):
    s = [-1]
    m = 0
    for i in range(n):
        if a[i] == '(':
            s.append(i)
        else:
            s.pop()
            if s!=[]:
                m = max(i-s[-1],m)
            else:
                s.append(i)
            # print(s,m)
    print(m)
t = int(input())
for _ in range(t):
    a = list(input())
    n = len(a)
    (result(a,n))
