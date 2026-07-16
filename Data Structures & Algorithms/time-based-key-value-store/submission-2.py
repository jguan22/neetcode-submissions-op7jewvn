class TimeMap:
    # store in a hash map, and binary search through the time since time is sorted

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add value: O(1)
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # edge case: key not exist
        if key not in self.timeMap:
            return ""
        
        value_list = self.timeMap[key]
        l, r = 0, len(value_list)

        # binary to find the first val larger than target: O(logn)
        while l < r:
            mid = (l + r) // 2
            if value_list[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid
        
        # left pointer will be 0 if no such target exists
        return value_list[l-1][0] if l > 0 else ""