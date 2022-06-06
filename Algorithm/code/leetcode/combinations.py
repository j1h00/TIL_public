# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []
        def dfs(n, k, prev, comb):
            if len(comb) == k:
                answer.append(comb)
                return 

            for i in range(prev + 1, n+1):
                if i not in comb:
                    dfs(n, k, i, comb + [i])
            
        dfs(n, k, 0, [])

        return answer


#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# pythonic 

import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


# recursive (k - 1)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return 

# list comprehension => 어렵다..
class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]