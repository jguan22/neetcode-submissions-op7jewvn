# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre_group = dummy
        curr = dummy
        
        while curr:
            count = 0
            # find the list to reverse
            while curr and count < k:
                curr = curr.next
                count += 1
                
            if not curr:
                break

            # mark the pre and next group
            next_group = curr.next
            pre = next_group
            start = pre_group.next
            curr = start
        
            # reverse the list
            while curr != next_group:
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp

            pre_group.next = pre
            
            # reset for next group
            pre_group = start
            curr = start
    
        return dummy.next