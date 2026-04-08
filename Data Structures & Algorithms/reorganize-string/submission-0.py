class Solution:
    def reorganizeString(self, s: str) -> str:
        # use heap to construct string with higher freq char first
        # use prev to track last used char
        freqMap = Counter(s)
        max_heap = [(-freq, c) for c, freq in freqMap.items()]
        heapq.heapify(max_heap)
        res = ""
        prev = None

        while max_heap or prev:
            # base case: no more char in heap but prev left to place
            if not max_heap and prev:
                return ""

            freq, char = heapq.heappop(max_heap)
            res = res + char
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if freq + 1 < 0:
                prev = (freq+1, char)
        
        return res