class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project_list = sorted(zip(capital, profits))
        i = 0

        available_projects = []
        for _ in range(k):
            while i < len(project_list) and w >= project_list[i][0]:
                heapq.heappush(available_projects, - project_list[i][1])
                i += 1
            
            if not available_projects:
                break
            
            curr = -heapq.heappop(available_projects)
            w += curr

        return w