class ListNode:

    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class DoubleLinkedList:

    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def add(self, node):
        prev =  self.tail.prev
        prev.nxt, node.prev = node, prev
        node.nxt, self.tail.prev = self.tail, node
    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.cache = DoubleLinkedList()
        self.node_map = defaultdict(ListNode)
        
    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        # update the node and move to the back: O(1)
        node = self.node_map[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # case 1: key exists
        if key in self.node_map:
            # update the val and move to the back: O(1)
            node = self.node_map[key]
            node.val = value
            self.update(node)
        else:   
            # case 2: key doesn't exist: O(1)
            new_node = ListNode(key, value)
            
            # remove lru if cache is full
            if self.capa == 0:
                # remove LRU and add 
                self.removeLRU()
            
            # add node to cache and update
            self.cache.add(new_node)
            self.node_map[key] = new_node
            self.capa -= 1

    def update(self, node):
        self.cache.remove(node)
        self.cache.add(node)
    
    def removeLRU(self):
        lru = self.cache.head.nxt
        self.cache.remove(lru)
        del self.node_map[lru.key]
        self.capa += 1