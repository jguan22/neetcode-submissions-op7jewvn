class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # use enqueue_heap to track task to enqueue (enqueueT, i)
        # use process_heap to track task to process (processT, i)
        enqueue_heap = [(enqueueT, i) for i, (enqueueT, _) in enumerate(tasks)]
        heapq.heapify(enqueue_heap)
        process_heap = []
        res = []
        time = 1
        while enqueue_heap or process_heap:
            if not process_heap and enqueue_heap[0][0] > time:
                time = enqueue_heap[0][0]
                
            if process_heap:
                processT, i = heapq.heappop(process_heap)
                res.append(i)
                time += processT
            
            while enqueue_heap and enqueue_heap[0][0] <= time:
                _, i = heapq.heappop(enqueue_heap)
                heapq.heappush(process_heap, (tasks[i][1], i))
        
        return res