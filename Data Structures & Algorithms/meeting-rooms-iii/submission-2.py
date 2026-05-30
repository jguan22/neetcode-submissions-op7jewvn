class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use a min heap to track available rooms
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        used_rooms = []     # track (end_time, room_index)
        meetings.sort()
        room_count = [0] * n

        for (start, end) in meetings:
            # 1. check if any curr meeting ends
            while used_rooms and used_rooms[0][0] <= start:
                _, i = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, i)
            
            # 2. pick a room if there is any
            if available_rooms:
                room_index = heapq.heappop(available_rooms)
            else:   # pick next available room with earliest end time
                end_time, room_index = heapq.heappop(used_rooms)
                end = end + (end_time - start)

            # 3. update used room and count 
            heapq.heappush(used_rooms, (end, room_index))
            room_count[room_index] += 1

        max_count = max(room_count)
        for i, count in enumerate(room_count):
            if count == max_count:
                return i
        return -1       