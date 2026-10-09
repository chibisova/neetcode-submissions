# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = k 
        output = root.val

        def dfs(node):
            nonlocal order, output
            if not node:
                return

            dfs(node.left)
            if order == 0:
                return
            order -= 1
            if order == 0:
                output = node.val
                return
            dfs(node.right)

        dfs(root)
        return output