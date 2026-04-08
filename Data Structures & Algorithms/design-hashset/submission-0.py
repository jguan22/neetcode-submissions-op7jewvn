class MyHashSet:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        # keep the list sorted
        index = self.findKey(key)
        if index < len(self.list) and self.list[index] == key:
            return

        self.list.insert(index, key)

    def remove(self, key: int) -> None:
        # binary search the key
        index = self.findKey(key)
        if index < len(self.list) and self.list[index] == key:
            self.list.pop(index)

    def contains(self, key: int) -> bool:
        index = self.findKey(key)
        return index < len(self.list) and self.list[index] == key
    
    def findKey(self, key: int) -> int:
        # helper function to find the key or the position to insert the key
        l, r = 0, len(self.list)
        while l < r:
            mid = (l + r) // 2
            if self.list[mid] >= key:
                r = mid
            else:
                l = mid + 1
        return l
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)