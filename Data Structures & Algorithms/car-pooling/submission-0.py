class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        # heap to track the trip (to, numP)
        heap = []

        for trip in trips:
            # unload passengers when arrives
            while heap and trip[1] >= heap[0][0]:
                _, numP = heapq.heappop(heap)
                capacity += numP
            
            # load passengers
            if trip[0] > capacity:
                return False
            capacity -= trip[0]
            heapq.heappush(heap, (trip[2], trip[0]))
        
        return True