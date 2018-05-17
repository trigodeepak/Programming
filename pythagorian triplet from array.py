def result(a,n):
    #sorting the squared array
    a.sort()
    #finding is their a triplet exist such that sum of 2 is third element
    # Done it using hashing technique
    for i in range(n-1,1,-1):
        s = a[i]
        d = {}
        for j in range(i):
##            print (d)
            if a[j] not in d:
                d[s-a[j]] = True
            else:
                return 'Yes'
    return 'No'

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = [i*i for i in a]
    print(result(a,n))

'''Sample Input
1
5
3 2 4 6 5
'''
