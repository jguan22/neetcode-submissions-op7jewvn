class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # keep tracking on the direction of arr
        last_dir = 0
        longest = 1
        n = len(arr)

        curr_len = 1
        for i in range(1, n):
            # + is increasing, - is decreasing, 0 is equal
            curr_dir = arr[i] - arr[i-1]
            if curr_dir == 0:
                curr_len = 1
            elif last_dir * curr_dir >= 0:  # same direction
                # reset len
                curr_len = 2
            else:
                curr_len += 1
            
            longest = max(longest, curr_len)
            last_dir = curr_dir
        
        return longest