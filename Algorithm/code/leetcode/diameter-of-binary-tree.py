# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. 
# This path may or may not pass through the root.

# https://blog.myungwoo.kr/112  트리의 지름 구하는 법 
# boj 1167

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # 현재 root 를 기준으로, 
        # 왼쪽 노드의 최대 깊이와 오른쪽 노드의 maximum depth 를 서로 더한다.
        # => revcursive 
        
        # depth()
        # 현재 노드를 기준으로 maximum depth 를 return 하고 
        # 함수 내부에서, answer 를 업데이트 한다.
        return 


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# recursive dfs 
# 현재 노드를 기준으로 왼쪽 리프 노드와 오른쪽 리프 노드 사이의 거리.. 

# leaf node 
# returns left + right + 2 
# ==> -1 + -1 + 2 = 0 
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left) 
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)  
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest


# leaf node 
# returns left + right 
# ==> 0 + 0 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def depth(p): # returns max(left-depth, right-depth)
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right) # left depth + right depth 
            return 1 + max(left, right)
            
        depth(root)
        return self.ans
            

            

            
        


