# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid of the list using fast/slow pointer
        dummy = ListNode(0, head)
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half starting from slow.next
        pre = None
        curr = slow.next
        
        # MUST: to prevent cycle
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        # merge two lists
        list1 = head
        list2 = pre
        while list1 and list2:
            temp = list1.next
            list1.next = list2
            list1 = temp
            temp = list2.next
            list2.next = list1
            list2 = temp
