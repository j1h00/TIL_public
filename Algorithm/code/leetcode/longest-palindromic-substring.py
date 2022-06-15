# https://leetcode.com/problems/longest-palindromic-substring/


# works for odd length palindrome
# but not for even like "abba", "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        max_len = 0
        max_str = ''

        for i in range(N):
            left = i-1 # even 경우에도 성립하게 하기 위해선, left 가 i 일 때의 경우를 나누어 해결한다. 
            right = i+1
            
            cur_len = 1
            while 0 <= left and right < N:
                if s[left] != s[right]:
                    break 

                cur_len += 2

                left -=1 
                right += 1

            cur_str = s[left + 1: right] 

            if cur_len > max_len:
                max_len = cur_len
                max_str = cur_str
                
        return max_str

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1), # even case "bb"
                         expand(i, i + 2), # odd case "aba"
                         key=len)
        return 