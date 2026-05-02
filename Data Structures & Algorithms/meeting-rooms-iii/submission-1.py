class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        # use a heap to track available rooms, lower num always on the top
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        freq_room = [0] * n

        # use a heap to track the used room (end, i)
        used_rooms = []
        
        for i in range(len(meetings)):
            start, end = meetings[i]

            while used_rooms and used_rooms[0][0] <= start:
                _, j = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, j)
            
            if not available_rooms:
                last_end, index = heapq.heappop(used_rooms)
                start, end = end, last_end + (end - start)
            else:
                index = heapq.heappop(available_rooms)
            
            heapq.heappush(used_rooms, (end, index))
            freq_room[index] += 1
        
        max_freq = 0
        ans = -1
        for i, freq in enumerate(freq_room):
            if freq > max_freq:
                max_freq = freq
                ans = i

        return ans