# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bfs_queue = [root]
        while(len(bfs_queue) > 0):
            current = bfs_queue.pop(0)
            last = current.val
            if(current.right):
                bfs_queue.append(current.right)
            if(current.left):
                bfs_queue.append(current.left)
        return last


# metadata
# relevant-topics right to left bfs, binary tree, recursion
# time-complexity O(N) 90.14%
# space-complexity O(N) 79.63%
# language python
# difficulty medium
# date 20240228