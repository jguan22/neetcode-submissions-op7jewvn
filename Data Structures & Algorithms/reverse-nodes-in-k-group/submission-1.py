# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = end = dummy
        # check if there is a group of k ahead
        while True:
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
                    
            end = self.reverse(start, k)
            start = end
        
    
    # reverse the list in a group of k in place
    def reverse(self, pre, k):
        curr = pre.next
        nxt = curr.next

        for _ in range(k-1):
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = curr.next

        # return the tail after reverse    
        return curr