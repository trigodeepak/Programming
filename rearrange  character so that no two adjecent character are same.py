#program to rearrange the characters so that no two adjecent
#character are same
def result(a,n):
    from collections import defaultdict
    d = defaultdict(int)
    for i in a:
        d[i]+=1
    q =[]
    for i in d:
        q.append((-d[i],i))
    import heapq
    heapq.heapify(q)
##    print (q)
    f = False
    l = 0
    s = []
    try :
        while True:
            if not f:
                if l < n:
                    s.append(q[0][1])
                    q[0] = (q[0][0]+1,q[0][1])
                    if q[0][0] == 0:
                        q.pop(0)
                        f = not f
                    f = not f
                    l+=1
                else:
                    print (1)
                    return 
            else:
                if l < n:
                    s.append(q[1][1])
                    q[1] = (q[1][0]+1,q[1][1])
                    if q[1][0] == 0:
                        q.pop(1)
##                        f = not f
                    f = not f
                    l+=1
                else:
                    print (1)
                    return
            heapq.heapify(q)
##            print (s,q,f)
    except:
        print (0)
        return 
    
t = int(input())
while t > 0:
    a = input()
    n = len(a)
    result(a,n)
    t-=1
