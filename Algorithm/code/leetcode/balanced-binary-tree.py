# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True 
        
        def height(node):
            if not node:
                return 0 

            return max(height(node.left), height(node.right))  + 1

        # check if root left and root right isBalanced
        if abs(height(root.left) - height(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        else:
            return False


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

#
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root): # return height
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


         
        

