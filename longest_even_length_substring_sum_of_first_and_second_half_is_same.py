#finding the longest string whose sum of first half and second half is same
a = "1538023"
a = [int(i) for i in a]
n = len(a)
k = 0
m = 0
while(k<n):
    i = 0
    j = k
    while(j<n):
        if (j-i % 2) != 0 and i!=j:
            b = j/2
            if sum(a[i:b+1]) == sum(a[b+1:j+1]) :
                m = max(m,j-i+1)
                
        i+=1
        j+=1
    k+=1
print m

