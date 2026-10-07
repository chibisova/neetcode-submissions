# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        output = 0
        def dfs(node, previous):
            nonlocal output
            if not node:
                return None

            if node.val >= previous:
                output += 1
                previous = node.val
            right, left = dfs(node.right, previous), dfs(node.left,  previous)
            
        dfs(root,root.val)
        return output

