class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        i = 0
        count = 0
        while count < n:
            pre = nums[i]
            index = i
            while True:
                index = (index + k) % n
                pre, nums[index] = nums[index], pre
                count += 1
                if index == i:
                    break
            
            i += 1
        return