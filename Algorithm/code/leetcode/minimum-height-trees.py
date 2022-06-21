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

#