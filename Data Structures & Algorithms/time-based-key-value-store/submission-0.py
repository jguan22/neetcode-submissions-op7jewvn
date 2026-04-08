class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create a list if key is not there yet
        if key not in self.dict:
            self.dict[key] = []
        
        self.dict[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        # use binary search
        arr = self.dict[key]
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid][0] > timestamp:
                hi = mid
            else:
                lo = mid + 1
            
        return arr[lo - 1][1] if lo > 0 else ""