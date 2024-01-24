# Runtime
# 330ms
# Beats 98.67% of users with Python3

# Memory
# 43.62MB
# Beats 96.44% of users with Python3

# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # print("0b110".count("1"))
        # return self.dfs(root, 1 << 10 | 1 << root.val)
        return self.dfs(root, 1 << root.val - 1)

    def dfs(self, node: Optional[TreeNode], path: int) -> int:

        # print("node val:",node.val, "pathArr:", pathArr)

        if node.left and node.right:
            # print("node.left and right do exist")
            lPath = path ^ (1 << node.left.val - 1)
            rPath = path ^ (1 << node.right.val - 1)
            return self.dfs(node.left, lPath) + self.dfs(node.right, rPath)
        elif node.right:
            # print("node.right does exist")
            path ^= 1 << (node.right.val - 1)
            return self.dfs(node.right, path)
        elif node.left:
            # print("node.left does exist")
            path ^= 1 << (node.left.val - 1)
            return self.dfs(node.left, path)
        else:
            # print("no child nodes")
            # print(bin(path))
            if str(bin(path)).count("1") < 2:
                # print('returning 1 with path ^^')
                return 1
            else:
                return 0
