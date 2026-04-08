class ListNode:

    def __init__(self, key, val):
        # use key of input as key and corresponding ListNode as val
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        # have a least and a most used end node
        self.least = ListNode(-1, -1)
        self.most = ListNode(-1, -1)
        self.least.next = self.most
        self.most.pre = self.least
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # locate the node by key
        # move the node to the most used by remove and add
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # update or add a new node
        # increment the size
        # pop least used node if necessary
        if key in self.cache:
            self._remove(self.cache[key])
            self.size -= 1
        node = ListNode(key, value)
        self.cache[key] = node
        self._add(node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.least.next
            self.cache.pop(lru.key)
            self._remove(lru)
            self.size -= 1


    def _add(self, node: ListNode):
        node.next = self.most
        node.pre = self.most.pre

        self.most.pre = node
        node.pre.next = node

    
    def _remove(self, node: ListNode):
        node.pre.next = node.next
        node.next.pre = node.pre