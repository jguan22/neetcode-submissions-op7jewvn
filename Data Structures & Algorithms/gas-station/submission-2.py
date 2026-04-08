class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sanity check
        if sum(gas) < sum(cost):
            return -1
        
        # keep going until cant reach next stop
        curr = 0
        start = 0
        for i in range(len(gas)):
            # reset at next stop if cant reach it
            if curr + gas[i] < cost[i]:
                curr = 0
                start = i + 1
            else:
                curr += (gas[i] - cost[i])
        
        return start