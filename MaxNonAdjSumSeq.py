#Program for Maximum sum subsequence non adjecent 
##a = map(int, raw_input().strip().split(' '))
a = [4,1,1,4,2,1]
inc = a[0]
excl = 0
n = len(a)
for i in range(1,n):
    temp = inc
    inc = max(inc,excl+a[i])
    excl = temp
    print inc, excl
#Answer is
print inc
