# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, i):
            if not root:
                return None
            
            if i == len(output):
                output.append([])
            
            output[i].append(root.val)

            left, right = dfs(root.left,i+1), dfs(root.right,i+1)

        output = [] 
        dfs(root, 0)
        return  output
