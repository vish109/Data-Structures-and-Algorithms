
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def level_order(root):
    result=[]
    q=[]
    q.append(root)
    while(q):
        q_len=len(q)
        level=[]
        for i in range(q_len):
            node=q.pop(0)
            if(node):
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if(level):
            result.append(level) 
    return result


root=TreeNode(7)
root.left=TreeNode(6)
root.right=TreeNode(5)
root.left.left=TreeNode(9)
root.left.left.left=TreeNode(2)
print(level_order(root))