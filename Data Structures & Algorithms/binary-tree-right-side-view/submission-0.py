# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(root, depth):
            if not root:
                return None
            
            if depth == len(output):
                output.append(root.val)
                
            right, left = bfs(root.right, depth + 1), bfs(root.left, depth + 1)


        output = []
        bfs(root, 0)
        return output