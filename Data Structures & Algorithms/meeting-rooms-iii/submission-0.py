class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use list to track the number of meeting for each room
        # one heap to track the available rooms
        # one heap to track the end_time of each taken room (end_time, room_index)
        meetings.sort()
        room_count = [0] * n
        avail_room = list(range(n))
        heapq.heapify(avail_room)
        room_schedule = []

        for i in range(len(meetings)):
            # clear the taken room when meeting is over
            while room_schedule and meetings[i][0] >= room_schedule[0][0]:
                _, room_index = heapq.heappop(room_schedule)
                heapq.heappush(avail_room, room_index)

            # take currently available room with smallest index
            if avail_room:
                room_index = heapq.heappop(avail_room)
                room_count[room_index] += 1
                heapq.heappush(room_schedule, (meetings[i][1], room_index))
                continue
            
            # if all rooms are taken, wait for the first available room
            first_avail_time, room_index = heapq.heappop(room_schedule)
            updated_end_time = meetings[i][1] + (first_avail_time - meetings[i][0])
            heapq.heappush(room_schedule, (updated_end_time, room_index))
            room_count[room_index] += 1
        
        # look for the room index with most used
        max_used = max(room_count)
        for i in range(n):
            if room_count[i] == max_used:
                return i
        
        return -1