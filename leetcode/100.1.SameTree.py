# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q):
            return True
        elif(p and q):
            return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False

# metadata
# relevant-topics binary tree, recursion
# time-complexity O(N) 70.24%
# space-complexity O(logN->N) 76.00%
# language python
# difficulty easy
# date 20240226