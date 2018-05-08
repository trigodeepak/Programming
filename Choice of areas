#Choice of different area at different step
#https://www.geeksforgeeks.org/game-theory-choice-area/
def result(a,areas,m,last):
    if a[0] > 0 and a[1] > 0:
        res = m
        print (a,areas)
        for i in range(3):
            if i != last:
                res = max(res,result([a[0]+areas[i][0],a[1]+areas[i][1]],areas,m+1,i))
        return res
    return 0
t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    n = int(input())
    areas = []
    for i in range(n):
        areas.append(list(map(int,input().split())))
    print(result(a,areas,0,-1))

''' Sample input 1) Take initial value of 2 areas and then taken number of area they can jump in?
1
20 8
3
3 2
-5 -10
-20 5
'''
