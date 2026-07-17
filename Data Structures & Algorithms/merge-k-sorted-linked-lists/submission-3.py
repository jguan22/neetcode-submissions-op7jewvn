# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use merge sort, split list to half recursively and merge them by 2: O(Nlogk)
        # helper to merge two list2
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            return dummy.next

        # base case:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        half = len(lists) // 2
        left = self.mergeKLists(lists[:half])
        right = self.mergeKLists(lists[half:])
        
        return merge(left, right)

        