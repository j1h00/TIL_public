# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 
            
            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# recursive
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None # may skip 

# stack 
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()  
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root

# bfs
import collections

def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        # 부모 노드 부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root