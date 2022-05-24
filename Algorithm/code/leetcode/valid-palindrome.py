# https://leetcode.com/problems/valid-palindrome/

from re import A


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
            j -= 1
            
        return True

                  
    
        
        

solution = Solution()

solution.isPalindrome("A man, a plan, a canal: Panama")

