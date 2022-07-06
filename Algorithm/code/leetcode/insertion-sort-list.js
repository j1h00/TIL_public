// https://leetcode.com/problems/insertion-sort-list/

// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var insertionSortList = function (head) {
  if (!head) return null;
  if (!head.next) return head;

  let sorted = head;
  let curr = head.next;
  sorted.next = null;

  while (curr) {
    const next = curr.next;
    const insertion = curr;

    output = insert(sorted, insertion);
    curr = next;
  }

  return sorted;
};

function insert(head, other) {
  let curr = head;
  const val = other.val;

  if (val <= head.val) {
    other.next = head;
    return other;
  }

  while (curr) {
    if ((val > curr.val && curr.next && val <= curr.next.val) || !curr.next) {
      other.next = curr.next;
      curr.next = other;

      return head;
    }

    curr = curr.next;
  }

  return head;
}

/*
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#
*/

// most viewed python solution converted to js
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var insertionSortList = function (head) {
  let dummyHead = new ListNode();
  let nodeToInsert = head;
  dummyHead.next = nodeToInsert;

  while (head && head.next) {
    if (head.val > head.next.val) {
      // pick up `nodeToInsert`
      nodeToInsert = head.next;
      head.next = nodeToInsert.next; // head.next.next

      // find where to insert `nodeToInsert`
      nodeToInsertPre = dummyHead;
      while (nodeToInsertPre.next.val < nodeToInsert.val) {
        nodeToInsertPre = nodeToInsertPre.next;
      }

      // insert
      nodeToInsert.next = nodeToInsertPre.next;
      nodeToInsertPre.next = nodeToInsert;

      continue;
    }

    head = head.next;
  }

  return dummyHead.next;
};
