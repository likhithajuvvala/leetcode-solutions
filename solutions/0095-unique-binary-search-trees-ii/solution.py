# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gentree(start, end):
            trees = []
            for i in range(start, end+1):
                left_trees = gentree(start, i-1) if i > start else [None]
                right_trees = gentree(i+1, end) if i < end else [None]
                trees += [TreeNode(i, ltree, rtree) for ltree, rtree in product(left_trees, right_trees)]
            return trees
        return gentree(1, n)