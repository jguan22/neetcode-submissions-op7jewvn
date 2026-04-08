class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        max_heap = [(-freq, c) for c, freq in freq_map.items()]
        heapq.heapify(max_heap)
        pre = None
        string = []
        while max_heap:
            freq, c = heapq.heappop(max_heap)
            string.append(c)

            if pre:
                heapq.heappush(max_heap, pre)
                pre = None
            
            if freq + 1 < 0:
                pre = (freq+1, c)
        
        return "".join(string) if not pre else ""