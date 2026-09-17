# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        visited = []
        visited.append(head)

        while head:
            if head.next:
                head = head.next
                next_val = head.val
            else:
                return False
            
            if head.val in visited:
                return True
            else:
                visited.append(head.val)
            head.next
        return False