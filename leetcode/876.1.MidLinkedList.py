# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        return slow
        
# metadata
# relevant-topics linked list, while loop, 2 pointers
# time-complexity O(N) 27.18%
# space-complexity O(1) 89.17%
# language python
# difficulty easy
# date 20240307