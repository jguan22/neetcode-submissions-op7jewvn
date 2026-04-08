class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x:x[1])
        n = len(projects)
        heap = []
        i = 0
        for _ in range(k):
            # put available projects into heap
            while i < n and projects[i][1] <= w:
                heapq.heappush(heap, (-projects[i][0], projects[i][1]))
                i += 1
            
            # do a project with higher profits
            if not heap: 
                return w
                
            profit, _ = heapq.heappop(heap)
            w += -profit
        
        return w