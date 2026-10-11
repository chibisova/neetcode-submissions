# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:  # curr is the current node we're processing
            
            temp = curr.next # temporarily save the next node so we don't lose the rest of the list
            curr.next = prev  # reverse the link: current node now points to the previous node
            prev = curr # move prev to the current node (new head of the reversed portion)
            curr = temp # move curr to the next node we still need to process
        return prev  # prev is the new head of the reversed list