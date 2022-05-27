# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = ''
        num2 = ''

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next 

        newNum = str(int(num1) + int(num2))

        cur = dummy = ListNode()
        for digit in newNum[::-1]:
            newNode = ListNode()
            newNode.val = digit

            cur.next = newNode 
            cur = newNode 

        return dummy.next
        
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0 # 현재 두 숫자의 합
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10 # 10보다 큰 경우 둘째 자리를 남긴다. 
        return dummy.next