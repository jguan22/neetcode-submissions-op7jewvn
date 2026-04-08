# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        pre = dummy
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            val = val % 10
            curr = ListNode(val)
            pre.next = curr
            pre = curr

        return dummy.next