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
    
    def add(self, node):
        pre = self.tail.pre
        pre.nxt, node.pre = node, pre
        node.nxt, self.tail.pre = self.tail, node
    
    def remove(self, node):
        pre, nxt = node.pre, node.nxt
        pre.nxt, nxt.pre = nxt, pre
    
    def isEmpty(self):
        return self.head.nxt == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        # need a list of linked lists to track freq of each node
        # a node map to track all nodes
        self.node_map = {}
        self.list_map = defaultdict(DLL)
        self.min_freq = 0
        self.capa = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.__updateNode(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # update freq and remove from pre list if node exists
        if key in self.node_map:
            node = self.node_map[key]
            self.__updateNode(node)
            node.val = value
        else: # make a new node if not
            node = ListNode(key, value)
            self.__addNewNode(node)
        

    def __addNewNode(self, node):
        # check if cache is full
        if self.size == self.capa:
            # remove lfu
            lfu_list = self.list_map[self.min_freq]
            lfu = lfu_list.head.nxt
            lfu_list.remove(lfu)
            del self.node_map[lfu.key]
        else:
            self.size += 1

        self.min_freq = 1
        self.list_map[1].add(node)
        self.node_map[node.key] = node

    
    def __updateNode(self, node):
        # remove from the list
        self.list_map[node.freq].remove(node)

        # update min_freq if that's the last node in min list
        if node.freq == self.min_freq and self.list_map[node.freq].isEmpty():
            self.min_freq += 1

        # update freq and put in new list
        node.freq += 1
        self.list_map[node.freq].add(node)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)