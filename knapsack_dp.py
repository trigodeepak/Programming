#Program for 0/1 knapsack problem
w = [1,3,4,5]
v = [1,4,5,7]
n = 7
c = [[0 for i in range(n+1)] for x in range(len(w))]

for i in range(len(w)):
    for j in range(n+1):
        if(i==0 and j==0):
            c[i][j]=0
        elif(j<w[i]):
            c[i][j]=c[i-1][j]
        else:
            c[i][j]= max(v[i]+c[i-1][j-w[i]],c[i-1][j])
for i in c:
    print i
#Last point is the answer 9 in this case
