#text justification
a = "Deepak Rao likes to code"
a = a.split()
length_array = [len(i) for i in a]
print (length_array)
n = len(a)
c = [[float('inf') for i in range(n)]for i in range(n)]
for i in range(n):
    for j in range(i,n):
        s = sum(length_array[i:j+1])+j-i
        if s<=10:
            c[i][j] = (10-s)**2
for i in c:
    print (i)

cost = [10*10]*n
real = [0]*n
cost[n-1] = c[n-1][n-1]
for i in range(n-1,-1,-1):
    cost[i] = c[i][4]
    for j in range(n-1,i-1,-1):
        cost[i] = min(cost[i],cost[j]+c[i][j-1])
print (cost)
