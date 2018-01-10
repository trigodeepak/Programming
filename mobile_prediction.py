#mobile prediction
a = "234"
a = list(a)
d = {'3': ['d', 'e', 'f'], '2': ['a', 'b', 'c'], '5': ['j', 'k', 'l'], '4': ['g', 'h', 'i'], '7': ['p', 'q', 'r','s'], '6': ['m', 'n', 'o'], '9': ['w', 'x', 'y','z'], '8': ['t', 'u', 'v']}
n = len(a)
res = []

def print_words_Util(a,n,res,i):
    if i == n:
        print "".join(res),
        return
    
    for j in xrange(len(d[a[i]])):
        if a[i] == '0' or a[i] == '1':
            return
        res.append(d[a[i]][j])
        print_words_Util(a,n,res,i+1)
        res.pop()

print_words_Util(a,n,[],0)
