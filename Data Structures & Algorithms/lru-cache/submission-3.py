class ListNode:

    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # need a dict to map val to node: easier to do add and delete
        self.node_map = {}

        # build the cache with a head and a tail node to track both end
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.capa = capacity

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        # pop from the list and insert
        node = self.node_map[key]
        self.__update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # node already exists
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.__update(node)
            return

        # pop lru if full
        if self.capa == 0:
            lru = self.tail.prev
            self.__delete(lru)
            del self.node_map[lru.key]
        
        node = ListNode(key, value)
        self.__add(node)
        self.node_map[key] = node
        
    def __update(self, node):
        self.__delete(node)
        self.__add(node)

    def __delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.capa += 1
    
    def __add(self, node):
        nxt = self.head.next
        node.prev, node.next = self.head, nxt
        self.head.next, nxt.prev = node, node
        self.capa -= 1