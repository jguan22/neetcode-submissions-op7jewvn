class ListNode:

    def __init__(self, key=0, val=0, pre=None, nxt=None):
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
    
    def isEmpty(self):
        return self.head.nxt == self.tail

    def add(self, node):
        pre = self.tail.pre
        pre.nxt, node.pre = node, pre
        self.tail.pre, node.nxt = node, self.tail

    def rm(self, node):
        pre, nxt = node.pre, node.nxt
        pre.nxt, nxt.pre = nxt, pre
        

class LFUCache:

    def __init__(self, capacity: int):
        # use a list of lists to represent each freq
        self.capa = capacity
        self.freq_list = defaultdict(DLL)
        self.node_map = {}
        self.min_freq = 1
        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self.updateNode(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.updateNode(node)
            return
        
        # remove lfu if cache is full
        if self.capa == 0:
            lfu = self.freq_list[self.min_freq].head.nxt
            self.freq_list[self.min_freq].rm(lfu)
            del self.node_map[lfu.key]
            self.capa += 1

        new_node = ListNode(key, value)
        self.node_map[key] = new_node
        self.freq_list[1].add(new_node)
        self.min_freq = 1
        self.capa -= 1
        

    def updateNode(self, node):
        # 1. remove from the pre list
        self.freq_list[node.freq].rm(node)
        if self.min_freq == node.freq and self.freq_list[node.freq].isEmpty():
            self.min_freq += 1

        # 2. update freq and move the new list
        node.freq += 1
        self.freq_list[node.freq].add(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)