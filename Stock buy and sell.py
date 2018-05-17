#Stock buy and sell 
def result(a,n):
    ans = []
    i = 0
    while i < n:
        j = i+1
        while j<n and a[j-1] < a[j]:
            j+=1
            if j == n:
                ans.append([i,j-1])
                return ans
        if (j-1 > i):
            ans.append([i,j-1])
        i = j
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    res = (result(a,n))
    if res == []:
        print ("No Profit",end = " ")
    for i in res:
        print("("+str(i[0])+' '+str(i[1])+")",end = " ")
    print ()
'''Sample input
2
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67
'''
