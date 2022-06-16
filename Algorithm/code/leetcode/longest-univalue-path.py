# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# failed at
# root = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 현재 노드를 기준으로, 
        # 하위 노드들을 dfs or bfs 로 탐색하자 => recursive dfs 가 편할 것 같다. 

        # 인접한 모든 노드들이 아니라, longest path 이므로 중복 방문하지 않는 경로를 찾아야 한다... 

        self.ans = 0
        if not root:
            return 0 

        def dfs(node):
            if not node: # 존재하지 않는 노드까지 탐색 
                return 0 

            count = 1 # 동일 경로에 포함되는 노드 개수 저장 
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 왼쪽 자식 노드와 같다면, count 에 노드 개수 추가
            if node.left and node.left.val == node.val: 
                count += left
            if node.right and node.right.val == node.val:
                count += right 
            
            self.ans = max(self.ans, count) 
            return max(left, right) + 1 if count > 1 else 1 

        dfs(root)
        return self.ans - 1
    

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# recursive dfs 
class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색 (until node is None)
            left = dfs(node.left) # 왼쪽 노드에서, 동일 경로의 최대 길이
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가 (자신도 포함하므로, 간선 추가)
            if node.left and node.left.val == node.val:
                left += 1 
            else:
                left = 0

            if node.right and node.right.val == node.val: 
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과 (왼쪽 경로와 오른쪽 경로 길이의 합)
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴 
            return max(left, right)

        dfs(root)
        return self.result
