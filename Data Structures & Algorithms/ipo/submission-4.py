class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # greedy: always take project with max profit currently
        # use a max heap to track available projects
        available_projects = []
        project_list = sorted(zip(capital, profits))
        i = 0
        n = len(project_list)

        # k is not guaranteed smaller than n
        while k > 0:
            # 1. move available projects to heap
            while i < n and project_list[i][0] <= w:
                heapq.heappush(available_projects, -project_list[i][1])
                i += 1
            
            # 2. pick the one with max profit
            if available_projects:
                p = heapq.heappop(available_projects)
                w += (-1 * p)
                k -= 1
            else:
                break
        
        return w