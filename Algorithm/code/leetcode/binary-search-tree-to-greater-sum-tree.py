# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# convert to =>  original key plus the sum of all keys greater than the original key in BST.
class Solution:
    stack = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 오른쪽 자식 노드 => 루트 => 왼쪽 자식 노드 순으로 돌면서 더해가면 될듯?
        if not root:
            return

        self.bstToGst(root.right)
        self.stack += root.val
        root.val = self.stack

        self.bstToGst(root.left)

        return root

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# short
val = 0
def bstToGst(self, root):
    if root.right: self.bstToGst(root.right)
    root.val = self.val = self.val + root.val
    if root.left: self.bstToGst(root.left)
    return root

# iterative
def bstToGst(self, root: TreeNode) -> TreeNode:
    if root:
        node, stk, sm = root, [], 0
        while node or stk:
            while node:
                stk.append(node)
                node = node.right
            node = stk.pop()
            node.val += sm
            sm = node.val
            node = node.left    
    return root

# reversed inorder
def bstToGst(self, root: TreeNode) -> TreeNode:
    
    def reversedInorder(node: TreeNode, sm: int) -> int:
        if node:
            node.val += reversedInorder(node.right, sm)
            return reversedInorder(node.left, node.val)
        return sm

    reversedInorder(root, 0)
    return root

