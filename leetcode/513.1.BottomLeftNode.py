# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if(not root.left and not root.right):
            return root.val
        if(self.depth(root.right) > self.depth(root.left)):
            return self.findBottomLeftValue(root.right)
        else:
            return self.findBottomLeftValue(root.left)

# metadata
# relevant-topics binary tree, recursion
# time-complexity O(N^2) 5.16%
# space-complexity O(N) 97.42%
# language python
# difficulty medium
# date 20240228