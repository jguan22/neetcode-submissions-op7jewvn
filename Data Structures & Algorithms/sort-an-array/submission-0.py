class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort

        def mergeSort(curr):
            n = len(curr)
            if n <= 1:
                return curr
            
            left = mergeSort(curr[:(n//2)])
            right = mergeSort(curr[(n//2):])

            leftLen = len(left)
            rightLen = n - leftLen
            i = j = 0
            res = []
            while i < leftLen and j < rightLen:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            if i < leftLen:
                res.extend(left[i:])
            if j < rightLen:
                res.extend(right[j:])
            return res

        return mergeSort(nums) 