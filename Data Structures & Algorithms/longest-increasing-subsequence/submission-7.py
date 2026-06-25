class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # maintain a stricly increasing stack
        n = len(nums)
        subseq = []

        # find the right spot in stack to insert num O(n logn)
        for num in nums:
            if not subseq or num > subseq[-1]:
                subseq.append(num)
                continue

            # binary search to find the spot
            l, r = 0, len(subseq) - 1
            while l < r:
                mid = (l + r) // 2
                if num > subseq[mid]:
                    l = mid + 1
                else:
                    r = mid
            
            subseq[l] = num
        
        return len(subseq)