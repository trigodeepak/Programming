#Highway billboard problem
x = [6, 9, 12, 14]
r = [5, 6, 3, 7]
m = 20
t = 2
n = len(x)
dp = [0]*m
j = 0
for i in xrange(x[0],m):
    if j<n:
        if x[j] != i:
            dp[i] = dp[i-1]
            continue
        else:
            if i<=t:
                dp[i] = max(dp[i-1],r[j])
            else:
                dp[i] = max(dp[i-t-1]+r[j],dp[i-1])
            j+=1
    else:
        print i,dp[x[0]:i]
        break
print "Answer is here : ",dp[i-1]
