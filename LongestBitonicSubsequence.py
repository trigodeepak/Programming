#Program for Longest Bitconic Sequence
##a = map(int, raw_input().strip().split(' '))
a = [1, 11, 2, 10, 4, 5, 2, 1]
#First we calculate lis from both sides then find the max value from it 
def lis_len(a):
    n = len(a)
    c = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if (a[i]>a[j]):
                c[i]= max(c[i],c[j]+1)
    return c
c1 = lis_len(a)
a = a[::-1]
c2 = lis_len(a)
for i in range(len(a)):
    c1[i]+=c2[i]-1
print max(c1)
