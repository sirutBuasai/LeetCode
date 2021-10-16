"""
   6.         7
 4   8.     2   8
1 5 7 9.   1 3    9
"""

class BST:
    def __init__(self, val=0):
        self.val = val
        self.l = self.r = None
        
onel = BST(4)
onel.l = BST(1)
onel.r = BST(5)
oner = BST(8)
oner.l = BST(7)
oner.r = BST(9)
one = BST(6)
one.l = onel
one.r = oner

twol = BST(2)
twol.l = BST(1)
twol.r = BST(3)
twor = BST(8)
twor.r = BST(9)
two = BST(7)
two.l = twol
two.r = twor

def dfs(tree1, tree2, arr):
    if not tree1:
        return
    else:
        find_elem(tree1.val, tree2, arr)
        dfs(tree1.l, tree2, arr)
        dfs(tree1.r, tree2, arr)

def find_elem(elem, tree, arr):
    if not tree:
        return
    elif elem == tree.val:
        arr.append(elem)
    elif elem > tree.val:
        find_elem(elem, tree.r, arr)
    else:
        find_elem(elem, tree.l, arr)

def dup_elem(tree1, tree2):
    result = []
    dfs(tree1, tree2, result)
    return result
    
print(dup_elem(one, two))
