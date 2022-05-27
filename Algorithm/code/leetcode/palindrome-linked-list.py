# https://leetcode.com/problems/palindrome-linked-list/ 
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        now = head
        node_list = []
        while now.next:
            node_list.append(now.val)
            now = now.next
        node_list.append(now.val)
        
        for i in range(len(node_list) // 2):
            if node_list[i] != node_list[-i-1]:
                return False

        return True 

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# most viewed answer 
# Solution 1: Reversed first half == Second half?
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev
