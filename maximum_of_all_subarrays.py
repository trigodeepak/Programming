#Maximum of all subarrays
a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
m = max(a[:k])
n = len(a)
print m,
for i in range(k,n):
    #this condition will check if the max element is out of the range
    if a[i-k] == m:
##        print "executing"
        m = max(a[i-k:i])
    if a[i]>m:
        m = a[i]
    print m,
