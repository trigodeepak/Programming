#Actually Logic of this is not correct for correct implementation using heap see
#https://github.com/trigodeepak/Programming/blob/master/maximum_of_all_subarrays_using_heap.py
#Program for maximum of all sub arrays 
a= [1,2,3,1,4,5,2,3,6]
##a = [8,5,10,7,9,4,15,12,90,13]
n = len(a)
k = 3
c = [0 for i in xrange(n-k+1)]
c[0] = max(a[:k])
for i in xrange(1,n-k+1):
    if(a[k+i-1]>c[i-1]):
        c[i] = a[k+i-1]
    else:
        c[i] = c[i-1]
print c
#This will print the list with elements having the greatest
#number from the subarray starting at that position 
# Ans : [3, 3, 4, 5, 5, 5, 6] in this case
