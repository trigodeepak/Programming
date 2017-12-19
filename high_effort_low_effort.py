#high effort vs low effort task
h = [3, 6, 8, 7, 6]
l = [1, 5, 4, 5, 3]
n = len(l)
task_dp = [0 for i in xrange(n+1)]
task_dp[1] = h[0]
i = 1
while(i<=n):
    task_dp[i] = max(h[i-1]+task_dp[i-2],l[i-1]+task_dp[i-1])
    i+=1
print task_dp
