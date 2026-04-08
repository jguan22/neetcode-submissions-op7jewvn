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
        if head is None:
            return None
        # create a copy list interweave with the original one
        curr = head

        # deal with next pointer fist: A->A'->B
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next
        
        # loop again to deal with random pointer
        new_head = head.next
        curr = head

        while curr:
            # 1.set random p
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        while curr:
            # 2.move next p
            copy = curr.next
            curr.next = copy.next
            curr = curr.next

            if copy.next:
                copy.next = curr.next

        
        return new_head