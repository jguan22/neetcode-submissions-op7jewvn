# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy

        curr = start
        while True:
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            if not curr or count != k:
                break

            curr = start.next
            for _ in range(k-1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = start.next
                start.next = nxt
            
            start = curr
        
        return dummy.next