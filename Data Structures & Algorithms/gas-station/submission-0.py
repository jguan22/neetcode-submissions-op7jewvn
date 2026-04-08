class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        def dfs(node, gas_vol):
            if visited[node]:
                return True
            
            visited[node] = True

            gas_vol += gas[node]
            gas_vol -= cost[node]

            if gas_vol >= 0:
                return dfs((node+1) % n, gas_vol)
            else:
                return False
    

        for i in range(n):
            visited = [False] * n
            if dfs(i, 0):
                return i
        
        return -1