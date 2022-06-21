# https://leetcode.com/problems/minimum-height-trees/


from typing import List
import collections


# failed
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # 모든 노드를 시작점으로 depth 구해보자 
        graph = collections.defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        height = [0] * n
        for start in range(n):
            q = collections.deque([(start, 0)])
            visited = [0] * n
            
            while q:
                now, depth = q.popleft()
                height[start] = depth 

                for nxt in graph[now]:
                    if not visited[nxt]:
                        q.append((nxt, depth + 1))
        
        return filter(lambda x: x == min(height), height)

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


# most viewed 
# https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
# AMAZING!! two pointer from leaf nodes  
# Any node that has already been a leaf cannot be the root of a MHT, because its adjacent non-leaf node will always be a better candidate.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves