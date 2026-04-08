class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # need to have a max_heap to schedule task with higher freq fist
        # need a queue to sequence the task based on cooldown time
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        queue = deque()

        time = 0
        while max_heap or queue:
            time += 1

            # each time check heap first. always schedule the higher freq
            if max_heap:
                # decrement the count (increment since its neg)
                count = heapq.heappop(max_heap) + 1

                # push in the queue to wait for cooldown
                if count < 0:
                    queue.append((count, time + n))
            
            # check queue next to pop any ready-to-run task
            while queue and queue[0][1] <= time:
                count, _ = queue.popleft()
                heapq.heappush(max_heap, count)
        
        return time