# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [0, root]
        level = 0
        last = -1
        while(len(q) > 0):
            current = q.pop(0)
            if(type(current) == type(0)):
                if(level % 2 == 0):
                    last = -1
                else:
                    last = 10**6 + 2
                if(len(q) > 0):
                    level += 1
                    q.append(level)
                continue
            if(level % 2 == 1):
                if(current.val % 2 == 0 or current.val <= last):
                    return False
            else:
                if(current.val % 2 == 1 or current.val >= last):
                    return False
            last = current.val
            if (current.left):
                q.append(current.left)
            if (current.right):
                q.append(current.right)
        return True

# metadata
# relevant-topics bfs, binary tree, queue
# time-complexity O(N) 26.95%
# space-complexity O(N) 90.74%
# language python
# difficulty medium
# date 20240229