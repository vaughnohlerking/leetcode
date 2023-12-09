# Runtime
# 39ms
# Beats 49.54%of users with Python3

# Memory
# 16.39MB
# Beats 19.15%of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.recurse(root)

    def recurse(self, root: Optional[TreeNode]) -> List[int]:
        if hasattr(root, "val"):
            val = [root.val]
        else:
            val = []
        if hasattr(root, "left"):
            left = self.recurse(root.left)
        else:
            left = []
        if hasattr(root, "right"):
           right = self.recurse(root.right)
        else:
            right = []

        return left + val + right
