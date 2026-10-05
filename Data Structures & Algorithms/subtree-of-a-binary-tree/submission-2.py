# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # an empty tree is considered a subtree of any tree
        if not subRoot:
            return True 
         # main tree is empty, but subRoot is not
        if not root:
            return False
        
        # check if subRoot matches the tree starting at this node
        if self.sameTree(root, subRoot):
            return True

        # if not, search in the left and right subtrees
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root:Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # both trees reached the end at the same time 
            # → they are identical
            if not root and not subRoot: 
                return True

            # current nodes exist and have the same value 
            # → continue checking their children
            if root and subRoot and root.val == subRoot.val: 
                # both left AND right subtrees must also be identical
                return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)) 

            # values differ, or one tree ended before the other
            return False 