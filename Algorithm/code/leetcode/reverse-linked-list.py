# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 다른 답안과 비교해봤을 때, 대체로 내 코드가 많이 지저분하다..
        if not head:
            return head

        prev, cur = head, head.next
        prev.next = None
        temp = ListNode() 
        temp.next = cur

        while cur:
            temp.next = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp.next

        return prev
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


# simple iterative 
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

# recursive 
class Solution:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)