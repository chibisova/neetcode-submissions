# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        output = 0
        def bfs(node, depth, previous):
            nonlocal output
            if not node:
                return None

            if node.val >= previous:
                output += 1
                previous = node.val
            right, left = bfs(node.right, depth + 1, previous), bfs(node.left, depth + 1, previous)
            
        bfs(root, 0, root.val)
        return output

