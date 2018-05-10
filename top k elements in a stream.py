#top k elements in a stream
import heapq
def result(a,n,k):
    from collections import defaultdict
    freq = defaultdict(int)
    top = [0]*(k+1)
    for m in range(n):
        freq[a[m]] += 1
        top[k] = a[m]
  
        i = top.index(a[m])
        i -= 1
         
        while i >= 0: 
            # compare the frequency and swap if higher
            # frequency element is stored next to it
            if (freq[top[i]] < freq[top[i + 1]]):
                t = top[i]
                top[i] = top[i+1]
                top[i + 1] = t
             
            # if frequency is same compare the elements
            # and swap if next element is high
            elif ((freq[top[i]] == freq[top[i+1]]) and (top[i] > top[i + 1])):
                t = top[i]
                top[i] = top[i+1]
                top[i + 1] = t
            else:
                break
            i -= 1
        # print top k elements
        i = 0
        while i < k and top[i] != 0:
            print (top[i],end = ' ')
            i += 1
    print ( )

t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    result(a,n,k)
