# merge-two-sorted-lists
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, and list2 are already sorted 
        # 너무 복잡하게 작성했다.. => 처음에 head 를 초기화하는 방법이 잘못되었다. 
        cur = dummy = ListNode() # head 앞에 dummy 를 두어 초기화하자
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 
                list1, cur = list1.next, list1 
            else:
                cur.next = list2
                list2, cur = list2.next, list2 

        if list1 or list2: # 굳이 while loop 돌지 않아도, 하나만 next 로 추가해주면 뒤에는 알아서 따라온다. 
            cur.next = list1 if list1 else list2

        return dummy.next
            

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# most viewed 
# 방법은 똑같은데, 코드가 훨씬 깔끔하다 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() 
        while list1 and list2:               
            if list1.val < list2.val: 
                cur.next = list1
                list1, cur = list1.next, list1 # update list1 & cur
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next # head