class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        def add(num, char):
            if num > 0:
                heapq.heappush(max_heap, (-num, char))
        
        add(a, 'a')
        add(b, 'b')
        add(c, 'c')

        res = []

        while max_heap:
            freq, c = heapq.heappop(max_heap)

            # choose the most freq char unless last two are the same
            if len(res) > 1 and res[-1] == c and res[-2] == c:
                # stop if there isn't any more char left
                if not max_heap:
                    return "".join(res)

                freq2, c2 = heapq.heappop(max_heap)
                res.append(c2)
                heapq.heappush(max_heap, (freq, c))
                if freq2 + 1 < 0:
                    heapq.heappush(max_heap, (freq2 + 1, c2))
            else:
                res.append(c)
                if freq + 1 < 0:
                    heapq.heappush(max_heap, (freq + 1, c))
            
        
        return "".join(res)