# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder): 
                return None # No preorder nodes left to construct

            if inorder[inIdx] == limit: 
                inIdx += 1 # Consume the inorder boundary node
                return None # Stop building this subtree

            root = TreeNode(preorder[preIdx]) # Preorder gives the next root
            preIdx += 1 # Consume this preorder value

            root.left = dfs(root.val) # Build left subtree up to this root's boundary
            root.right = dfs(limit) # Build right subtree up to the inherited boundary
            return root
        return dfs(float('inf'))

        