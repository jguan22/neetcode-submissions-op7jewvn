# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first half of the list move forward and second half move backward, then merge them interleaved
        # use slow and fast pointers to find the half point: O(n)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half: O(n)
        pre = slow
        curr = pre.next

        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        
        # merge list2 with list1: O(n)
        list1 = head
        list2 = pre.next
        pre.next = None

        while list1 and list2:
            temp = list1.next
            list1.next = list2
            list1 = temp
            
            temp = list2.next
            list2.next = list1
            list2 = temp
        
        return
