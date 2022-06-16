# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive?
        if not root:
            return 0 

        if not root.left and not root.right:
            return 1

        if root.left and not root.right:
            return self.maxDepth(root.left) + 1 
        
        if root.right and not root.left:
            return self.maxDepth(root.right) + 1
        
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


# recursive DFS 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)

# recursive without new function 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# queue
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth



