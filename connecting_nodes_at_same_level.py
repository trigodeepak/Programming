#Program for connecting the nodes at the same level
class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.next = None
        self.val=key
root=node(1)
root.left=node(2)
root.right=node(3)
root.right.right=node(4)
root.left.left=node(5)

def connect_level(root):
    q = [root]
    while len(q) > 0:
        n = len(q)
        for k in range(n):
            k = q.pop(0)
            if len(q) > 0 :
                k.next = q[0]
            else :
                k.next = None
            if k.left != None:
                q.append(k.left)
            if k.right != None:
                q.append(k.right)

def traverse_in(root):
    if root == None :
        return
    traverse_in(root.left)
    print (root.val,root.next)
    traverse_in(root.right)
connect_level(root)
traverse_in(root)
