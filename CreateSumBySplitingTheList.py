n = input()
a = map(int,raw_input().strip().split(' '))
b=[0 for i in range(n)]
#to create pieces of the array
b[0]= a[0]
def createSum(a,p,i):
    s=0
    if(p<i):
        for j in range(p,i):
            s+=createSum(a,j,i)
        return s
    else:
        return a[i]
for i in range(1,n):
    b[i]=(a[i-1]+createSum(a,0,i))
print b   
#not working properly stacktrace is keep on coming  https://digitalunlocked.withgoogle.com/topic/1/assessment  
