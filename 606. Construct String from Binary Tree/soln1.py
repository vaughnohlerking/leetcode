# Runtime
# 53ms
# Beats 54.27%of users with Python3

# Memory
# 18.88MB
# Beats 50.54%of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      return self.recurse(root)

    def recurse(self, root: Optional[TreeNode]) -> str:
      if root.left == None and root.right == None:
        return str(root.val)
      elif root.left == None and root.right != None:
        return str(root.val)+"()("+self.recurse(root.right)+")"
      elif root.left != None and root.right == None:
        return str(root.val)+"("+self.recurse(root.left)+")"
      else:
        return str(root.val)+"("+self.recurse(root.left)+")("+self.recurse(root.right)+")"
