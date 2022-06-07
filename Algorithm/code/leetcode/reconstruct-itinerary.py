# https://leetcode.com/problems/reconstruct-itinerary/

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        prev = {}
        next = {}

        for ticket in tickets:
            start, end = ticket
            next[start] = next.get(start, []) + [end]
            prev[end] = prev.get(end, []) + [start]

        for start in next:
            next[start].sort()
        
        print(next)

        path = ['JFK']
        results = []

        def dfs(path):
            print(path)
            now = path[-1]
            if (now not in next) or (not next[now]):
                results.append(path)
                return 

            nxt = next[now].pop()
            dfs(path + [nxt])
            next[now].append(nxt)

        dfs(path)
        return results[0]


            
