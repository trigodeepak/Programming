#search the element in a sorted and pivoted array
a = [5,6,7,8,9,10,1,2,3]
n = len(a)
def binarySearch(a,first,last,item):
    if(last<first):
        return -1
    mid = (first+last)/2
    if(item == a[mid]):
        return mid
    elif(item>a[mid]):
        return binarySearch(a,mid+1,last,item)
    return binarySearch(a,first,mid-1,item)

#Function to find the pivot where the array is separating 
def findPivot(a,low,high):
    if (high<low):
        return -1
    if(high==low):
        return low

    mid = (low+high)/2
    if(mid < high and a[mid]>a[mid+1]):
        return mid;
    elif(mid > low and a[mid]<a[mid-1]):
        return mid-1;
    elif (a[low]>=a[mid]):
        return findPivot(a,low,mid-1)
    else:
        return findPivot(a,mid+1,high)

def pivotedBinarySearch(a,n,item):
    pivot = findPivot(a,0,n-1)
    if(a[pivot]==item):
        return pivot
    elif(a[0]<item):
        return binarySearch(a,0,pivot-1,item)
    else:
        return binarySearch(a,pivot+1,n-1,item)
        
print pivotedBinarySearch(a,n,7)
