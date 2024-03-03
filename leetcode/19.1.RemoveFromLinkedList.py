# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        total = 0
        while(curr):
            total += 1
            curr = curr.next
        if (total - n == 0):
            return head.next
        curr = head
        for i in range(0, total - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

# metadata
# relevant-topics linked list, while loop, for loop
# time-complexity O(N) 72.40%
# space-complexity O(1) 61.49%
# language python
# difficulty medium
# date 20240303