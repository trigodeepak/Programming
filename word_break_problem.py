#word break problem using recursion
d = ["mobile","samsung","sam","sung","mango","icecream","and","i","like","ice","cream"]
a = "ilikesamsung"

def wordbreak(a,res,d,n,i):
    if i == -1:
        s = [len(i) for i in res]
        if sum(s)==len(a):
            res = res[::-1]
            for j in res:
                print j,
            print 
        return

    if a[i:n+1] in d:
        res.append(a[i:n+1])
        wordbreak(a,res,d,i-1,i-1)
        res.pop()
        wordbreak(a,res,d,n,i-1)
    else:
        wordbreak(a,res,d,n,i-1)
n = len(a)
wordbreak(a,[],d,n-1,n-1)
        
  
