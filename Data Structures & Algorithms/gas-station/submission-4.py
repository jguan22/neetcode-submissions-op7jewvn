class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sanity check: gas must be larger than cost
        if sum(gas) < sum(cost):
            return -1
        
        # if not, there is guaranteed to be one valid answer
        # linear scan to track on the remaining gas vs nxt cost: O(n)
        # start over when not enough gas to go on
        start_index = 0
        remaining_gas = 0
        n = len(gas)
        for i in range(n):
            remaining_gas += gas[i]
            remaining_gas -= cost[i]
            if remaining_gas < 0:
                start_index = i + 1
                remaining_gas = 0
        
        return start_index