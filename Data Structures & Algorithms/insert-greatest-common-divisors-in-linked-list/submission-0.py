from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre, curr = dummy, head
        while curr and curr.next:
            pre, curr = curr, curr.next
            divisor = gcd(pre.val, curr.val)
            new_node = ListNode(divisor, curr)
            pre.next = new_node
        
        return dummy.next