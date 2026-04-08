class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project_queue = deque(sorted(zip(capital, profits), key=lambda x: x[0]))
        available_projects = []

        while k > 0:
            while project_queue and project_queue[0][0] <= w:
                _, p = project_queue.popleft()
                heapq.heappush(available_projects, -p)
            
            if not available_projects:
                break
                
            w -= heapq.heappop(available_projects)
            k -= 1
        
        return w