# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        N = len(digits)

        digit_to_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if not digits:
            return answer 

        def dfs(comb, idx):
            if idx >= N:
                answer.append(comb)
                return 

            nowDigit = digits[idx]
            for letter in digit_to_letter[nowDigit]:
                dfs(comb + letter, idx + 1)

        dfs('', 0)
        
        return answer

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


# use nested for loops 
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

# shorter
def letterCombinations(self, digits):
    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in dict[d]]
    return cmb