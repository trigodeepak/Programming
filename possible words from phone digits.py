#print possible words from phone digits
def result(a,n,ind,s):
    global res
    # print(ind)
    if len(s) == n:
        # print(s)
        res.append(''.join(s))
        return
    for k in d[a[ind]]:
        # print(k,d[a[i]])
        s.append(k)
        result(a,n,ind+1,s)
        s.pop()
        
d = {}
a = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]
for i in range(10):
    d[i] = list(a[i])
res = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    (result(a,n,0,[]))
    print(' '.join(res))
    res = []
