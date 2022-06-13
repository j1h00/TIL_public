# https://leetcode.com/problems/network-delay-time/
from typing import List
from collections import defaultdict, deque

# bfs 
# faster than 95%
class Solution: 
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)        
        for s, e, w in times:
            edges[s].append((e, w))

        q = deque([(k, 0)])
        time = [0] + [10 ** 6] * (n) # may use float('inf') instead 
        time[k] = 0
        while q:
            now, total = q.popleft()

            for nxt, w in edges[now]:
                if time[nxt] > total + w:
                    time[nxt] = total + w
                    q.append((nxt, total + w))
        
        if max(time) == 10 ** 6:
            return -1 
        
        return max(time)

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

import collections 
import heapq

# heap => Dijkstra 
class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1

# bfs => shortest path
class Solution:
    def networkDelayTime(self, times, N, K):
        t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1
                
