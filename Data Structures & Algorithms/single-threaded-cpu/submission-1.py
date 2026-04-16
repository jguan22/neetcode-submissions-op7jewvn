class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [(enqueueT, i) for i, [enqueueT, _] in enumerate(tasks)]
        heapq.heapify(task_list)

        op_list = []
        available_tasks = []
        t = task_list[0][0]
        while task_list or available_tasks:
            if not available_tasks and task_list[0][0] > t:
                t = task_list[0][0]

            while task_list and task_list[0][0] <= t:
                _, i = heapq.heappop(task_list)
                heapq.heappush(available_tasks, (tasks[i][1], i))
            
            if available_tasks:
                processT, i = heapq.heappop(available_tasks)
                op_list.append(i)
                t += processT
        
        return op_list