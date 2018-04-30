from collections import defaultdict
import sys
#Maximum sum submatrix in a given matrix
#https://www.hackerrank.com/contests/programming-pathshala1/challenges/submatrix-query
n,m = map(int, sys.stdin.readline().split(' '))
a = []
for i in range(n):
    a.append(map(int, sys.stdin.readline().split(' ')))
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            a[i][j] +=  a[i][j-1]
        elif j == 0:
            a[i][j] += a[i-1][j]
        else:
            a[i][j] += a[i-1][j] + a[i][j-1] - a[i-1][j-1]
            
b = [[0 for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        b[j][i] = a[i][j]
##for i in a:
##    print i
##for i in b:
##    print i

t = input()
for i in xrange(t):
    q = map(int, sys.stdin.readline().split(' '))
    q[1]-=1
    q[2]-=1
    s = []
    size = 0
    if q[0] == 0:
        size = n
        if q[1]!=0:
            s.append(a[0][q[2]]-a[0][q[1]-1])
            for i in xrange(1,n):
                s.append(a[i][q[2]]-a[i-1][q[2]]-a[i][q[1]-1]+a[i-1][q[1]-1])
        else:
            s.append(a[0][q[2]])
            for i in xrange(1,n):
                s.append(a[i][q[2]]-a[i-1][q[2]])
        
    else:
        size = m
        if q[1]!=0:
            s.append(a[q[2]][0]-a[q[1]-1][0])
            for i in xrange(1,m):
                s.append(a[q[2]][i]-a[q[2]][i-1]-a[q[1]-1][i]+a[q[1]-1][i-1])
        else:
            s.append(a[q[2]][0])
            for i in xrange(1,m):
                s.append(a[q[2]][i]-a[q[2]][i-1])
    #Khadane's algorithm
    max_so_far = -float('inf')
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + s[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    print max_so_far

'''Sample input
3 3
1 -2 4
5 -9 2
-1 0 0
2
0 2 3
1 1 2
'''
