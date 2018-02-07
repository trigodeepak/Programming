#program to sort an array according to frequency
a = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
#creating dictionary 
dict = {}
for i in a:
    if dict.has_key(i):
        dict[i]+=1
    else:
        dict[i]=1
b = []
for i in dict:
    b.append((i,dict[i]))
b = sorted(b,key=lambda x: x[1],reverse=True)
a = []
for i in b:
    a+= [i[0]]*i[1]
print a
