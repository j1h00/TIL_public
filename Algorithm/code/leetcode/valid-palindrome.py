# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""
        for i in range(len(s)):
            decimal = ord(s[i])
            if 48 <= decimal <= 57 or 97 <= decimal <= 122:
                newStr += s[i]

        i, j = 0, len(newStr) - 1 
        while i <= j:
            if newStr[i] != newStr[j]:
                return False

            i += 1
            j -= 1s
            
        return True

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# most viewed answer 
class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():  # 영어, 한글, 숫자일 경우 True, else false 
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True

# use regex
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱

# short 
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
