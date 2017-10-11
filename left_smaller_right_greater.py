#program for left smaller and right greater
a = [5, 1, 4, 3, 6, 8, 10, 7, 9]
left = []
left.append(a[0])
right = []
right.append(a[-1])
n = len(a)
for i in xrange(1,n):
    if(left[i-1]<a[i]):
        left.append(a[i])
    else:
        left.append(left[i-1])
    if(right[i-1]>a[n-1-i]):
        right.append(a[n-1-i])
    else:
        right.append(right[i-1])
#reversing the right array
right = right[::-1]
for i in xrange(n):
    if left[i] == right[i]:
        print left[i]
