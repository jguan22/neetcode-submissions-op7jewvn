class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # always pick the task with the most count
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        max_heap = [(-freq, task) for task, freq in freq.items()]
        heapq.heapify(max_heap)

        # need to have a queue to track cooldown (t, -freq, task)
        queue = deque()
        t = 0
        while max_heap or queue:
            # check cooldown queue
            while queue and queue[0][0] == t:
                _, freq, task = queue.popleft()
                heapq.heappush(max_heap, (freq, task))
            
            # pick a task to do
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                freq += 1
                if freq < 0:
                    queue.append((t+n+1, freq, task))
            
            t += 1
        
        return t