# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        res = 0

        def dfs(root):
            nonlocal res # to use outside res

            if not root:
                return 0
            
            right = dfs(root.right) # check if there is right node
            left = dfs(root.left) # check if there is left node

            res = max(res, left + right) # length between left and right at the moment

            return 1 + max(left, right) # return the deeper one

        dfs(root)
        return res