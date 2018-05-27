#merge sort
a = [2, 4, 1, 3, 5]
def merge(low,mid,high):
    global a
    b = []
    l1 = low
    l2 = mid+1
    print (low,mid,high)
    while l1<=mid and l2<=high:
        if a[l1]<=a[l2]:
            b.append(a[l1])
            l1+=1
        else:
            b.append(a[l2])
            l2+=1
            
    for i in range(l1,mid+1):
        b.append(a[i])

    for i in range(l2,high+1):
        b.append(a[i])
        
    a[low:high+1]=b
    
        
def sort(low, high):
    if low<high:
        mid = (low+high)//2
        sort(low,mid)
        sort(mid+1,low)
        merge(low,mid,high)

sort(0,len(a)-1)
print(a)
    
