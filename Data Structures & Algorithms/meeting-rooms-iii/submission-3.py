class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # total time complexity is: O(mlogm + mlogn)
        # 1. use unused room with lowest num: use a min heap to track
        # 2. if no available rooms, wait for the next one: use a min heap to track ending time of each curr meeting
        # 3. meeting with earlier original start time goes first: sort the meeting list by start time
        meetings.sort()     # O(mlogm)
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        used_rooms = []     # (end, i)
        room_count = [0] * n     # track room usage

        # loop through all meetings and maintain two heaps: O(m * logn)
        for start, end in meetings:
            # 1. move used rooms to available rooms if meeting is over
            while used_rooms and used_rooms[0][0] <= start:
                _, i = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, i)
            
            # 2. take a room if any available
            if available_rooms:
                i = heapq.heappop(available_rooms)
                room_count[i] += 1
                heapq.heappush(used_rooms, (end, i))
            else:
                # 3. if no room available, wait for the next available one
                new_start, i = heapq.heappop(used_rooms)
                room_count[i] += 1

                new_end = new_start + (end - start)
                heapq.heappush(used_rooms, (new_end, i))
        
        # find the room index with the lowest count: O(n)
        max_count = max(room_count)
        for i, count in enumerate(room_count):
            if count == max_count:
                return i
        return -1