class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # count sort
        left = min(nums)
        right = max(nums)
        num_freq = [0] * (right - left + 1)
        for num in nums:
            num_freq[num-left] += 1
        
        count = 0
        for i in range(len(num_freq)-1, -1, -1):
            count += num_freq[i]
            if count >= k:
                return i + left