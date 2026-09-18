# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head) # a dummy node wiht a random value 0 and link to the next value - head

        left = dummy #prev
        right = head #cur

        # move right pointer to len(head) - n
        while n > 0 and right:
            right = right.next
            n -= 1

        # update pointers, until we reach the end with right pointer
        while right:
            left = left.next
            right = right.next

        # remove target element
        left.next = left.next.next

        #return updated list
        return dummy.next