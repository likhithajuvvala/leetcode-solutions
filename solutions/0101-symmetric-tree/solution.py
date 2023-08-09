# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        def symmetric(l,r):
            if l is None and r is None :
                return True
            if l is None or r is None:
                return False
            return l.val==r.val and symmetric(l.left,r.right) and symmetric(l.right,r.left)
        return symmetric(root,root)
    