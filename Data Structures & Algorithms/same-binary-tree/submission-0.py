# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([q])
        p1 = deque([p])

        while q1 and p1:
            for _ in range(len(q1)):
                nodeP = p1.popleft()
                nodeQ = q1.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
            
                p1.append(nodeP.left)
                p1.append(nodeP.right)
                q1.append(nodeQ.left)
                q1.append(nodeQ.right)
        return True