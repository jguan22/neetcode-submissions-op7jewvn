"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case:
        if not head:
            return None

        # make a copy node right next to the original node: O(n)
        curr = head
        while curr:
            copy = Node(curr.val, curr.next, None)
            curr.next = copy
            curr = copy.next
        
        # deal with random pointers: O(n)
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # disconnect copy with origin: O(n)
        copy_head = head.next
        curr = head
        
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next
        
        return copy_head
