# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next

        arr.sort()

        node = head
        for i in range(len(arr)):
            node.val = arr[i]
            node = node.next
        return head

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# merge sort 사용
class Solution:
    # 두 정렬 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용 => https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%9F%B0%EB%84%88-%EA%B8%B0%EB%B2%95
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)