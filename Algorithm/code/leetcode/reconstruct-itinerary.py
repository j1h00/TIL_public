# https://leetcode.com/problems/reconstruct-itinerary/

import collections
from typing import List

# FAILED
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        next = {}

        for ticket in tickets:
            start, end = ticket
            next[start] = next.get(start, []) + [end]

        for start in next:
            next[start].sort(reverse = True)

        path = ['JFK']
        results = []

        def dfs(path):
            now = path[-1]
            if (now not in next) or (not next[now]):
                results.append(path)
                return 

            candidates = next[now][:]
            for nxt in candidates:
                next[now].remove(nxt)
                dfs(path + [nxt])
                next[now].append(nxt)

        dfs(path)
        return 


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        # 1. ["JFK","SFO"], 2. ["JFK","ATL"] ...  
        for a, b in sorted(tickets, reverse = True): 
            graph[a].append(b)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop()) # 1. ATL, 2. SFO
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]

# stack
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets, reverse = True):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        # 다시 뒤집어 어휘순 결과로
        return route[::-1]