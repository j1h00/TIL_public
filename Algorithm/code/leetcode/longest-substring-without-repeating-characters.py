# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# https://velog.io/@kgh732/Python-%EC%9C%BC%EB%A1%9C-%ED%91%B8%EB%8A%94-Leetcode3.-Longest-Substring-Without-Repeating-Characters
# sliding window 를 이용한 풀이 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left_cursor = 0
        used = {}
        
        for right_cursor, char in enumerate(s):
            if char in used and left_cursor <= used[char]: # left ~ right 문자열 중에 중복이 포함된 경우
                left_cursor = used[char] + 1 # 중복이 등장한 이후부터 다시 찾기 시작
                # 이 경우 left cursor 가 뒤로 건너뛰게 되므로, 조건의 left_cursor <= used[char] 이 필요함
            else:
                ans = max(ans, right_cursor - left_cursor + 1)
            used[char] = right_cursor # 가장 최근 위치를 업데이트
            
        return ans

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# 위와 동일하다. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length