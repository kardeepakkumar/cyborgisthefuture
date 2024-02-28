# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bfs_queue = [root, "lvl"]
        result = root.val
        update = False
        while(len(bfs_queue) > 0):
            current = bfs_queue.pop(0)
            if(type(current) == type("lvl")):
                update = True
                continue
            if(update):
                result = current.val
                bfs_queue.append("lvl")
                update = False
            if(current.left):
                bfs_queue.append(current.left)
            if(current.right):
                bfs_queue.append(current.right)
        return result


# metadata
# relevant-topics bfs, binary tree, recursion
# time-complexity O(N) 33.46%
# space-complexity O(N) 79.63%
# language python
# difficulty medium
# date 20240228