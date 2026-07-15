class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # to achieve log runtime, need to do binary search directly
        # need to figure out where to split two sorted arrays so that combine of left part is what we need
        # binary the shorter array: nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # median means half of numbers on the left or left has half + 1
        n, m = len(nums1), len(nums2)
        half = (n + m + 1) // 2

        # binary split nums1: log(min(m, n))
        l, r = 0, n
        while l <= r:
            # once split nums1, the split of nums2 is determined as well
            split1 = (l + r) // 2
            split2 = half - split1

            # if split is 0, everything is on the right, so the max left is -inf
            # if split is n, everything is on the left, so the min right is inf
            max_left1 = nums1[split1-1] if split1 > 0 else float('-inf')
            min_right1 = nums1[split1] if split1 < n else float('inf')

            max_left2 = nums2[split2-1] if split2 > 0 else float('-inf')
            min_right2 = nums2[split2] if split2 < m else float('inf')

            # verify curr split to ensure smallest of right part 1 is bigger than largest of left part 2
            # also, smallest of right part 2 is bigger than largest of left part 1
            if min_right1 >= max_left2 and min_right2 >= max_left1:
                # if total is odd, there is exact one median
                if (n + m) % 2 == 1:
                    return float(max(max_left1, max_left2))
                else:   # otherwise, median is the average
                    max_left = max(max_left1, max_left2)
                    min_right = min(min_right1, min_right2)
                    return (max_left + min_right) / 2.0
            elif min_right1 < max_left2:
                # case of small nums show in the large part, move right
                l = split1 + 1
            else:
                # case of large nums show in the small part, move left
                r = split1 - 1