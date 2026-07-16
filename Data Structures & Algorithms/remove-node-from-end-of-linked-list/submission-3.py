# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers to find the node: O(n)
        dummy = ListNode(0, head)
        slow = fast = dummy
        pre = None

        for _ in range(n):
            fast = fast.next
        
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        
        # remove the node
        pre.next = slow.next
        return dummy.next