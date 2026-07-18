class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy: always pick the highest freq tasks: O(n)
        freq_map = Counter(tasks)
        max_heap = [(-freq, task) for task, freq in freq_map.items()]
        heapq.heapify(max_heap)

        # need a cooldown queue (available time, task, freq)
        queue = deque()
        
        # loop until all tasks are processed: O(m*logn)
        t = 0
        while max_heap or queue:
            # pop any available task from queue
            while queue and queue[0][0] == t:
                _, task, freq = queue.popleft()
                heapq.heappush(max_heap, (freq, task))

            # pick a task with highest freq
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                freq += 1            
                if freq != 0:
                    queue.append((t + n + 1, task, freq))
                       
                t += 1
            else:   # otherwise, fastforward to next available time
                t = queue[0][0]

        return t