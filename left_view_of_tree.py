
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def left_view(root):
    result=[]
    q=[]
    q.append(root)
    while(q):
        q_len=len(q)
        for i in range(q_len):
            node = q.pop(0)
            if(node):
                if(i==0):
                    result.append(node.val)
                q.append(node.left)
                q.append(node.right)
    return result
    

root=TreeNode(7)
root.left=TreeNode(6)
root.right=TreeNode(5)
root.left.right=TreeNode(11)
root.left.left=TreeNode(9)
root.left.left.left=TreeNode(2)
print(left_view(root))