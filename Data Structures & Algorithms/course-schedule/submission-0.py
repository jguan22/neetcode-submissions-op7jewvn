class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        forward_list = defaultdict(list)
        for pre in prerequisites:
            forward_list[pre[0]].append(pre[1])

        
        def dfs(node):
            # base case: find a loop (edge towards a node in path)
            if node in inPath:
                return False

            # base case: visited already
            if node in checked:
                return True
            
            # mark node
            checked.add(node)
            inPath.add(node)

            # explore all neighbours
            for neighbour in forward_list[node]:
                if not dfs(neighbour):
                    return False
            inPath.remove(node)
            return True


        # run df: check if there is any cycle
        checked = set()
        for course in range(numCourses):
            if course not in checked:
                inPath = set()
                if not dfs(course):
                    return False
        
        return True