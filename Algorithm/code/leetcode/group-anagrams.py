# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. for str in strs:
        # 2. use set(str.split(""))
        # 3. set() 서로 비교 
        str_sets = []
        answer = {}
        for str in str:
            now_set = set(str.split(""))
            if now_set in str_sets:
                
            