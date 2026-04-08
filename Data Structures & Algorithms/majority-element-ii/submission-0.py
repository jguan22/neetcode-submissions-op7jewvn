class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        target = len(nums) / 3
        ans = []
        for num, freq in freq_dict.items():
            if freq > target:
                ans.append(num)
        
        return ans