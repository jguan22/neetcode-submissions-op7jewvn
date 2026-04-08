class Node:
    
    def __init__(self, key=0, val=0, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        # need a doubled linked list to maintain the order of cache
        # need a dict to look up node in the list (key, node)
        self.capa = capacity
        self.cache = {}

        # dummy nodes on both end for quick look up
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
    
    # helper to add node to the head of the list
    def _add(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node
    
    # helper to remove node from the list
    def _rm(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # move node to the front
        node = self.cache[key]
        self._rm(node)
        self._add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # update the value if key is there already
        if key in self.cache:
            self._rm(self.cache[key])
        
        # add node and update list and dict
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)

        # check capacity
        if len(self.cache) > self.capa:
            # list is full, remove the LRU
            node = self.tail.pre
            self._rm(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)