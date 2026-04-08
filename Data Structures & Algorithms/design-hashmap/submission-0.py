class MyHashMap:

    def __init__(self):
        # keep a sorted list as (key, value)
        self.list = []

    def put(self, key: int, value: int) -> None:
        index = self.findKey(key)
        if index < len(self.list) and self.list[index][0] == key:
            self.list[index][1] = value
        else:
            self.list.insert(index, [key, value])

    def get(self, key: int) -> int:
        index = self.findKey(key)
        if index < len(self.list) and self.list[index][0] == key:
            return self.list[index][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.findKey(key)
        if index < len(self.list) and self.list[index][0] == key:
            self.list.pop(index)

    def findKey(self, key):
        # helper function to find the key or position to insert the key
        n = len(self.list)

        # the most right boundary is n as key is larger than all elements
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            # find the min index to fulfil condition
            if self.list[mid][0] >= key:
                r = mid
            else:
                l = l + 1
        return l
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)