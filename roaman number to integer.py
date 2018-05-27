#Roaman number to integer
def result(a,n):
    s = d[a[0]]
    for i in range(1,n):
        s += d[a[i]]
        if d[a[i-1]]<d[a[i]]:
            s -= 2*d[a[i-1]]
        # print(s)
    print(s)
    
a = [('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)]
d = {}
for i in a:
    d[i[0]] = i[1]
# print(d)
t = int(input())
for _ in range(t):
    a = input()
    n = len(a)
    result(a,n)
