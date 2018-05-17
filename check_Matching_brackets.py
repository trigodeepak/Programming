def result(a,n):
    #python code for matching parenthesis
    a = list(a)
    stack = []
    l = len(a)
    f = 0
    for i in range(l):
        if a[i] in '{([':
            stack.append(a[i])
        elif stack == []:
            print ("not balanced")
            return
        elif a[i] == ')' and stack[-1] == '(' or a[i] == '}' and stack[-1] == '{' or a[i] == ']' and stack[-1] == '[':
            stack.pop()
        else:
            print ("not balanced")
            return
        
    if(stack == []):
        print ("balanced")
    else:
        print ("not balanced")

t = int(input())
for _ in range(t):
    a = input()
    n = len(a)
    (result(a,n))

'''Sample Input
3
{([])}
()
()[]
'''
