class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # keep tracking on the total gas and cost
        # and curr trip at the same time
        n = len(gas)
        total_gas = 0
        curr_gas = 0
        start = 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            # run out of gas, meaning curr trip doesn't work
            # start over from next point
            if curr_gas < 0:
                curr_gas = 0
                start = i + 1
        
        # we need more gas than total cost to complete a trip
        return start if total_gas >= 0 else -1