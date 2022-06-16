# https://leetcode.com/problems/valid-parentheses/


# use stack 
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        stack = []

        for chr in s:
            if stack and chr in pairs and pairs[chr] == stack[-1]:
                stack.pop() 
                continue

            stack.append(chr)
        
        if stack:
            return False
        
        return True 
            
#---------------------------------------------#
#--------------- Other Answers ---------------#
#---------------------------------------------#

# most viewed
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

# char in table
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0