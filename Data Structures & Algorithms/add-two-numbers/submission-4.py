# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        h1 = dummy
        add_next = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur_sum = v1 + v2 + add_next

            if cur_sum > 9:
                cur_sum = cur_sum - 10
                add_next = 1
            else:
                add_next = 0
            h1.next = ListNode(cur_sum)
            h1 = h1.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if add_next:
            h1.next = ListNode(add_next)
        return dummy.next