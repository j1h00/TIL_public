# https://leetcode.com/problems/course-schedule/
# prerequisites[i] = [ai, bi] 
# bi 를 수강하기 위해선, 먼저 ai 를 수강해야 한다.


import collections
from typing import List

# Failed 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre = collections.defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)

        path = set() 
        visited = set() # visited 를 통해 가지치기가 가능하다. 

        def dfs(now):
            if now in path: # 지나온 경로에 now 가 있는 경우, 즉 cycle 
                return False 

            if now in visited: # 이미 방문하여 True 로 체크된 경우 
                return True 

            path.add(now)
            for nxt in pre[now]:
                if not dfs(nxt):
                    return False
            path.remove(now)
            visited.add(now)

            return True 
            

        for a in list(pre):
            if not dfs(a):
                return False
                
        return True
         
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#
        
# use one visit Array 
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]

    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False
        
        if visit[i] == 1:
            return True

        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1

        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True