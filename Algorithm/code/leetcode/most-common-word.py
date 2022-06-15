# https://leetcode.com/problems/most-common-word/
from typing import List

# wrong !
# when case "a, a, a, a, b,b,b,c, c", ["a"] 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.lower().split(" ")
        word_dict = {}
        for word in words:
            newWord = ''
            for chr in word:
                if chr.isalpha():
                    newWord += chr 
            
            if newWord in word_dict:
                word_dict[newWord] += 1
                continue
                
            word_dict[newWord] = 1
            
        for word in sorted(word_dict.keys(), key = lambda x: -word_dict[x]):
            if word not in banned:
                return word
                break 
        

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# regex & pythonic 
import re 
import collections

class Solution:
   def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

# \w : alpha + numeric => [a-zA-Z0-9_] 
# \W : non-alphanumeric => [^a-zA-Z0-9_] 
# regex split
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = re.split(r'\W+', paragraph.lower())
        b = [w for w in a if w not in banned]
        return max(b, key = b.count)