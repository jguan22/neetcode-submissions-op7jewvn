class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the task list and enqueue task at enqueue time
        task_list = [[enqueueT, processT, i] for i, [enqueueT, processT] in enumerate(tasks)]
        task_list.sort()
        task_i = 0

        # use a min heap to pop available task with shortest porcessing time
        available_tasks = []    # (processT, index)
        process_order = []

        # start at t = 0 and loop until all tasks are processed
        t = 0
        while task_i < len(task_list) or available_tasks:
            # 1. enqueue tasks
            while task_i < len(task_list) and task_list[task_i][0] <= t:
                heapq.heappush(available_tasks, (task_list[task_i][1], task_list[task_i][2]))
                task_i += 1
            
            # 2. enqueue the next task if heap is empty
            if not available_tasks:
                # curr time move to the enqueue time of next task
                t, processT, index = task_list[task_i]
                heapq.heappush(available_tasks, (processT, index))
                task_i += 1

            # 3. cpu takes a task
            processT, index = heapq.heappop(available_tasks)
            t += processT
            process_order.append(index)
        
        return process_order