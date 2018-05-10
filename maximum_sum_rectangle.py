#Maximum sum rectangle in a matrix
def result(a,n,k):
    max_r = 0
    max_l = 0
    max_top = 0
    max_bot = 0
    curr_max = 0

    for l in range(k):
        b = [0]*n
        for r in range(l,k):
            #Khadane algorithm to find the maximum sum
            m = 0
            max_arr = 0
            st = 0
            e = 0
            s = 0
            for i in range(n):
                b[i] += a[i][r]
                m += b[i]
                if max_arr < m:
                    max_arr = m
                    st = s
                    e = i
                if m<0:
                    m = 0
                    s = i+1
            #To update the sum after each iteration
            if max_arr > curr_max:
                curr_max = max_arr
                max_top = st
                max_bot = e
                max_r = r
                max_l = l
    print (curr_max)
    
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i*m:(i+1)*m])
    a = b
    (result(a,n,m))
