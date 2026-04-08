class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        step = k % n

        ans = nums[(n-step):] + nums[:(n-step)]
        nums[:] = ans