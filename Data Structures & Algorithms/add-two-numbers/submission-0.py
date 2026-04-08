# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy

        while l1 and l2:
            sumup = l1.val + l2.val + carry
            carry = sumup // 10
            curr.next = ListNode(sumup % 10)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        while curr.next and carry:
            curr = curr.next
            sumup = curr.val + carry
            curr.val = sumup % 10
            carry = sumup // 10
                
        if carry:
            curr.next = ListNode(carry)


        return dummy.next