# https://leetcode.com/problems/merge-two-binary-trees/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# failed.. 어렵다
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):          
            node1.val += node2.val 

            if node1.left: 
                if node2.left:
                    dfs(node1.left, node2.left)
                else:
                    dfs(node1.left, TreeNode())
            else:
                if node2.left:
                    node1.left = TreeNode()
                    dfs(node1.left, node2.left)

            if node1.right: 
                if node2.right:
                    dfs(node1.right, node2.right)
                else:
                    dfs(node1.right, TreeNode())
            else:
                if node2.right:
                    node1.right = TreeNode()
                    dfs(node1.right, node2.right)

        if root2 and not root1:
            root1 = root2
            return

        dfs(root1, root2)

        return root1
        

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#
            
                
#
def mergeTrees(self, t1, t2):
    if not t1 and not t2: return None
    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return ans


#
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2