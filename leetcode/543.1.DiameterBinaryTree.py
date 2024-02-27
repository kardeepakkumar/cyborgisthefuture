# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLength(self, root: Optional[TreeNode]):
        left, right = 0, 0
        if(root.left):
            left = 1+max(self.maxLength(root.left))
        if(root.right):
            right = 1+max(self.maxLength(root.right))
        return [left, right]
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left, right = self.maxLength(root)
        result = left + right
        if(root.left):
            result = max(self.diameterOfBinaryTree(root.left), result)
        if(root.right):
            result = max(self.diameterOfBinaryTree(root.right), result)
        return result

# metadata
# relevant-topics binary tree, recursion
# time-complexity O(N^2) 5.04%
# space-complexity O(N^2) 74.69%
# language python
# difficulty easy
# date 20240227