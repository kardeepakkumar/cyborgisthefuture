# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        depth(root)
        return self.diameter
    
# metadata
# relevant-topics binary tree, recursion
# time-complexity O(N) 28.23%%
# space-complexity O(N) 95.81%
# language python
# difficulty easy
# date 20240227