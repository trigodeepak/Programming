#snake and ladder using the graph theory
def make_dict(x):
    d = {}
    for i in x:
        d[i[0]] = i[1]
    return d

def make_graph(l,s):
    i = 1
    g = {}
    for i in xrange(1,100):
        ele = {}
        if i in l or i in s:
            g[i] = {}
            continue
        for j in xrange(6,0,-1):
            ele[j] = i+j
            if i+j in l :
                ele[j] = l[i+j]
            if i+j in s :
                ele[j] = s[i+j] 
        g[i] = ele
    return g

def bfs(i,l,g):
    s = 0
    q = [i]
    visited = [False]*110
    while len(q)>0:
        n = len(q)
        for j in xrange(n):
            node = q.pop(0)
            if node == 100:
                return s
            visited[node-1] = True
            for k in g[node]:
                if not visited[g[node][k]-1]:
                    q.append(g[node][k])
                    visited[g[node][k]-1] = True
        s+=1
    return -1
        

def quickestWayUp(ladders, snakes):
    l = make_dict(ladders)
    s = make_dict(snakes)
    g = make_graph(l,s)
    return bfs(1,100,g)
                

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        ladders = []
        for ladders_i in xrange(n):
            ladders_temp = map(int,raw_input().strip().split(' '))
            ladders.append(ladders_temp)
        m = int(raw_input().strip())
        snakes = []
        for snakes_i in xrange(m):
            snakes_temp = map(int,raw_input().strip().split(' '))
            snakes.append(snakes_temp)
        result = quickestWayUp(ladders, snakes)
        print result

