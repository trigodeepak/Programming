#Program for Cutting rod problem
##a = map(int, raw_input().strip().split(' '))

p = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(p)
c = [0 for i in range(n+1)]
for i in range(1,n+1):
    max_value=-1
    for j in range(i):
        c[i]= max(max_value,p[j]+c[i-j-1])
        max_value = c[i]
        
print c[n]
