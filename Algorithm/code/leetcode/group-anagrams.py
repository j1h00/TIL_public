# https://leetcode.com/problems/group-anagrams/

from typing import List

# failed..
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. for str in strs:
        # 2. use set(str.split(""))
        # 3. set() 서로 비교 
        return 
#
# dictionary 의 key 로 set 을 사용할 수 없으면, sort 해서 str 을 사용하자

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# pythonic
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())