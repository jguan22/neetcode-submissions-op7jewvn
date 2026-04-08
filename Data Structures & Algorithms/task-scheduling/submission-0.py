class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use dict to determine the number of each task
        task_dict = defaultdict(int)
        for task in tasks:
            task_dict[task] += 1
        
        max_heap = []
        for task in task_dict:
            # keep freq from high to low
            heapq.heappush(max_heap, -task_dict[task])
        
        # need a queue to help tracking cooldown (cooldown, freq)
        queue = deque([])
        time = 0
        while max_heap or queue:
            # check queue if heap is empty
            if not max_heap:
                cooldown, freq = queue.popleft()
                time = cooldown
                heapq.heappush(max_heap, freq)
            
            time += 1

            # always pick more freq task first
            freq = heapq.heappop(max_heap)
            freq += 1
            cooldown = time + n

            # push task in queue
            if freq < 0:
                queue.append((cooldown, freq))
            
            # pop any task available in queue
            while queue and queue[0][0] <= time:
                cooldown, freq = queue.popleft()
                heapq.heappush(max_heap, freq)
        
        return time