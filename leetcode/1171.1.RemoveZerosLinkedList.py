# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = head.val
        cur = head
        start = None
        while head:
            if total == 0:
                if not start:
                    head = cur.next
                else:
                    start.next = cur.next
                    start = None
                if not head:
                    break
                cur = head
                total = cur.val
            elif not cur.next:
                if not start:
                    start = head
                else:
                    start = start.next
                if not start.next:
                    break
                cur = start.next
                total = cur.val
            else:
                cur = cur.next
                total += cur.val
        return head
        
# metadata
# relevant-topics linked list
# time-complexity O(N^2) 5.18%
# space-complexity O(1) 53.78%
# language python
# difficulty medium
# date 20240312