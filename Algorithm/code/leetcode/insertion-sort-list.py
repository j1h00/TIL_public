# https://leetcode.com/problems/insertion-sort-list/


# most viewed 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(self, head):

  dummyHead = ListNode(0)
  dummyHead.next = nodeToInsert = head

  while head and head.next:
      if head.val > head.next.val:
          # Locate nodeToInsert.
          nodeToInsert = head.next
          # Locate nodeToInsertPre.
          nodeToInsertPre = dummyHead
          while nodeToInsertPre.next.val < nodeToInsert.val:
              nodeToInsertPre = nodeToInsertPre.next
              
          head.next = nodeToInsert.next
          # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
          nodeToInsert.next = nodeToInsertPre.next
          nodeToInsertPre.next = nodeToInsert
      else:
          head = head.next
      
  return dummyHead.next