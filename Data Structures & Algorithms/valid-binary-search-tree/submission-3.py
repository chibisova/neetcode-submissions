# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        min_l = float('-inf')
        max_r = float('inf')
        q.append((root, min_l, max_r))

        while q:
            node, min_l, max_r = q.popleft()

            if not (min_l < node.val < max_r):
                return False
            
            if node.left:                   
                q.append((node.left, min_l, node.val))

            if node.right:
                q.append((node.right, node.val, max_r))
            
        return True