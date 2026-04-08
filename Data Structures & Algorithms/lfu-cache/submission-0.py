class Node():

    def __init__(self, key=0, val=0, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.pre = pre
        self.next = nxt

# construct doubly linked list
class DLL():

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    def add(self, node):
        node.pre, node.next = self.head, self.head.next
        node.next.pre = node
        self.head.next = node
        self.size += 1
    
    def rm(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        # use a map to map key to node
        self.nodeMap = {}

        # use doubly linked list to store nodes with same freq
        # a map to map freq to each freq_list
        self.listMap = defaultdict(DLL)

        # keep track on the min freq (AKA the first list to pop node)
        # thus, LFU is sorted by map and LRU is sorted by list
        self.minFreq = 0
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self._updateNode(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        # check if its a new node
        if key not in self.nodeMap:
            self._addNewNode(key, value)
        else:
            self._updateNode(key, value)
            
    def _updateNode(self, key, value):
        node = self.nodeMap[key]
        node.val = value

        # remove from the curr freq list, update the minFreq if necessary
        self.listMap[node.freq].rm(node)
        if node.freq == self.minFreq and self.listMap[node.freq].size == 0:
            self.minFreq += 1
        
        # update freq and move node up
        node.freq += 1
        self.listMap[node.freq].add(node)

    def _addNewNode(self, key, value):
        # list is full, need to remove a node
        if len(self.nodeMap) == self.capacity:
            lfuList = self.listMap[self.minFreq]
            lfu = lfuList.tail.pre
            lfuList.rm(lfu)
            # delete the node from map
            del self.nodeMap[lfu.key]

        # add the new node
        newNode = Node(key, value)
        self.nodeMap[key] = newNode
        self.listMap[1].add(newNode)

        # reset the minFreq
        self.minFreq = 1            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)