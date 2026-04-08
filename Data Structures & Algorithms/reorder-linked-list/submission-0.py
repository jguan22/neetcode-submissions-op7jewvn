# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast-slow pointer to find mid point
        pre = None
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        # reverse the second half of the list
        pre = None
        curr = slow
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        # merge two lists
        list1 = head
        list2 = pre
        while list2.next:
            temp = list1.next
            list1.next = list2
            list1 = temp
            temp = list2.next
            list2.next = list1
            list2 = temp
        