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
        print("visited: ", visited)

        while head:
            if head.next:
                head = head.next
                next_val = head.val
                print("next_val: ", next_val)
            else:
                return False
            
            if head.val in visited:
                print("gotcha:", head.val)
                return True
            else:
                visited.append(head.val)
                print('Go next')
            head.next
        return False