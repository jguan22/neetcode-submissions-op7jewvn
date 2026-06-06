class ListNode:

    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        self.freq = 1   # initialize freq as 1

class DLL:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        nxt = self.head.next
        node.prev, self.head.next = self.head, node
        node.next, nxt.prev = nxt, node
    
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def isEmpty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        # use a list of doubled linked lists, each list for certain freq
        # then, need a dict to track lists and a dict to track nodes
        self.list_map = defaultdict(DLL)
        self.node_map = defaultdict(ListNode)

        # also, need to track least freq
        self.least_freq = 0
        self.capa = capacity

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self.__update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # update node if key exists
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.__update(node)
        else:
            # check if cache is full
            if self.capa == 0:
                # delete lfu
                lfu = self.list_map[self.least_freq].tail.prev
                self.list_map[self.least_freq].delete(lfu)
                del self.node_map[lfu.key]
                self.capa += 1
            
            # add new node
            new_node = ListNode(key, value)
            self.node_map[key] = new_node
            self.list_map[1].add(new_node)
            self.least_freq = 1
            self.capa -= 1
                
    
    def __update(self, node):
        # pop from curr freq list
        self.list_map[node.freq].delete(node)

        # update least_freq if necessary
        if self.list_map[node.freq].isEmpty() and node.freq == self.least_freq:
            self.least_freq += 1
        
        # increment freq and insert into new list
        node.freq += 1
        self.list_map[node.freq].add(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)