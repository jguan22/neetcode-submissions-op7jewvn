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
        # instead of direct copy, interweave the original nodes with new nodes first, then handle random pointers
        dummy = Node(-1, head, None)
        curr = head

        while curr:
            # copy the node with next pointer
            newNode = Node(curr.val, curr.next, None)
            curr.next = newNode
            curr = newNode.next
        
        curr = head
        while curr:
            # handle random pointer
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        if head:
            copy = head.next
        else:
            copy = None
        cpoyHead = copy
        while curr:
            # now reconstruct two lists' next pointers
            curr.next = copy.next
            curr = copy.next
            if curr:
                copy.next = curr.next
                copy = copy.next
        
        return cpoyHead