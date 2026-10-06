# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        prev_root = root

        while prev_root:
            if p.val > prev_root.val and q.val > prev_root.val:
                prev_root = prev_root.right
            elif p.val < prev_root.val and q.val < prev_root.val:
                prev_root = prev_root.left
            else:
                return prev_root
            
