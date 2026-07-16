# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointers
        slow = fast = head

        # loop through the list: O(n)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # loop detected
            if slow == fast:
                return True
        
        return False