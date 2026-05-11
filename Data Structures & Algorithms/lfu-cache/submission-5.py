class ListNode:

    def __init__(self, key=-1, val=-1, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
        self.freq = 1

class DLL:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt, self.tail.pre = self.tail, self.head
    
    def add(self, node):
        nxt = self.head.nxt
        self.head.nxt, node.pre = node, self.head
        node.nxt, nxt.pre = nxt, node

    def rm(self, node):
        pre, nxt = node.pre, node.nxt
        pre.nxt, nxt.pre = nxt, pre

    def isEmpty(self):
        return self.head.nxt == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        # use a double linked list for each freq and use a dict to track each freq
        self.freq_map = defaultdict(DLL)
        self.node_map = {}
        self.capa = capacity

        # keep track on the mini freq for a fast lfu removal
        self.min_freq = 0

    def get(self, key: int) -> int:
        val = -1
        if key in self.node_map:
            node = self.node_map[key]
            val = node.val
            self.__update(node)
            
        return val

    def put(self, key: int, value: int) -> None:
        # check if curr key already exists
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.__update(node)
        else:
            # evict lfu if cache is full
            if self.capa == 0:
                self.__deleteLFU()
            
            # create the new node, insert to freq 1 list and update all global variabes
            node = ListNode(key, value)
            self.node_map[key] = node
            self.freq_map[1].add(node)
            self.capa -= 1
            self.min_freq = 1
    
    def __deleteLFU(self):
        lfu_list = self.freq_map[self.min_freq]
        lfu = lfu_list.tail.pre
        self.__rm(lfu)
        del self.node_map[lfu.key]
        self.capa += 1
    
    def __update(self, node):
        # remove from curr freq list and update min_freq if necessary
        self.__rm(node)
        if self.freq_map[self.min_freq].isEmpty():
            self.min_freq += 1

        # update node freq and insert it to new list    
        node.freq += 1
        self.__add(node)
    
    def __add(self, node):
        freq_list = self.freq_map[node.freq]
        freq_list.add(node)

    def __rm(self, node):
        freq_list = self.freq_map[node.freq]
        freq_list.rm(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)