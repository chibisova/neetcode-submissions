"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        h1 = head # current head 
        while h1: # for every head repeat
            h2 = Node(h1.val) # save the value of current head (3)
            h2.next = h1.random # and it's random index (null)
            h1.random = h2 # put that 3:null into h1's random pointer 
            h1 = h1.next # and go to the next pointer
        # h1 = [[3,h2[0]], [7,h2[1]], [4,h2[2]], [5,h2[3]]]
        # h2 = [[3,next = null],[7,next = 3],[4,next = 0],[5,next = 1]]
        
        dc_head = head.random # h2[0]
        
        h1 = head # [3, h2[0]]
        while h1:
            h2 = h1.random
            h2.random = h2.next.random if h2.next else None
            h1 = h1.next

        h1 = head  # [3, h2[0]]
        while h1 is not None:
            h2 = h1.random
            h1.random = h2.next
            h2.next = h1.next.random if h1.next else None
            h1 = h1.next

        return dc_head