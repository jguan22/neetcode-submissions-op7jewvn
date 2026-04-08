# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointer, fast is n ahead of slow
        dummy = ListNode(0, head)
        pre, slow = dummy, head
        fast = head
        count = 0
        while count < n:
            fast = fast.next
            count += 1
        
        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next
        return dummy.next