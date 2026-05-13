class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # greedy: always take curr project with max profit
        projects = sorted(zip(capital, profits))
        available_projects = []
        n = len(projects)
        i = 0

        for _ in range(k):
            # 1. add available projects to heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(available_projects, -projects[i][1])
                i += 1
            
            # stop if no available projects
            if not available_projects:
                break 
                
            # 2. take curr max
            w -= heapq.heappop(available_projects)
        
        return w