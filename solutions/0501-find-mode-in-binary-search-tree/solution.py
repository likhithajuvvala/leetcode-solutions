# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = float('-inf')
        self.freq = 0
        self.max_freq = 0
        self.res = []

    def inOrder(self, node):
        if node is None:
            return

        self.inOrder(node.left)

        if self.val == node.val:
            self.freq += 1
        else:
            self.val = node.val
            self.freq = 1

        if self.freq > self.max_freq:
            self.max_freq = self.freq
            self.res = [node.val]
        elif self.freq == self.max_freq:
            self.res.append(node.val)

        self.inOrder(node.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inOrder(root)
        return self.res
        