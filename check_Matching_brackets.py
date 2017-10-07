#python code for matching parenthesis
a = "[()]{}{[()()]()}"
a = list(a)
stack = []
l = len(a)
i = 0
f=0
while(i<= l-1):
    print stack,a[i]
    if a[i] in '{([':
        stack = [a[i]] + stack
    elif a[i] == ')' and stack[0] == '(':
        stack.pop(0)
    elif a[i] == '}' and stack[0] == '{':
        stack.pop(0)
    elif a[i] == ']' and stack[0] == '[':
        stack.pop(0)
    else:
        print "failed"
        f = 1
        break
    i+=1
if(f==0):
    print "Match brackets"

