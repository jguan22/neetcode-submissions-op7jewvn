class ListNode:

    def __init__(self, key=-1, val=--1, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt

class DLL:

    def __init__(self, capacity):
        self.node_map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt, self.tail.pre = self.tail, self.head
        self.capa = capacity

    def add(self, key, val):
        if key not in self.node_map:
            node = ListNode(key, val)

            # if full, evict lru
            if self.capa == 0:
                lru = self.tail.pre
                pre = lru.pre
                pre.nxt, self.tail.pre = self.tail, pre
                del self.node_map[lru.key]
                self.capa += 1
            
            self._update(node)
            self.node_map[key] = node
            self.capa -= 1

        else:
            node = self.node_map[key]
            node.val = val
            self._update(node)
    
    def get(self, key):
        val = -1
        if key in self.node_map:
            node = self.node_map[key]
            self._update(node)
            val = node.val
        return val
    
    def _update(self, node):
        # 1. pop selected node
        if node.pre and node.nxt:
            pre, nxt = node.pre, node.nxt
            pre.nxt, nxt.pre = nxt, pre

        # 2. insert to the front
        nxt = self.head.nxt
        self.head.nxt, node.pre = node, self.head
        nxt.pre, node.nxt = node, nxt

class LRUCache:

    def __init__(self, capacity: int):
        # need to use a double linked list
        self.cache = DLL(capacity)

    def get(self, key: int) -> int:
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache.add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)