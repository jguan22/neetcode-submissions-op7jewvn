class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def mergeSort(curr_list):
            n = len(curr_list)
            if n == 0 or n == 1:
                return curr_list
            
            mid = n // 2
            left = mergeSort(curr_list[:mid])
            right = mergeSort(curr_list[mid:])

            sorted_list = []
            i, j = 0, 0
            left_len, right_len = mid, n - mid
            while i < left_len and j < right_len:
                if left[i] <= right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            
            if i < left_len:
                sorted_list.extend(left[i:])
            if j < right_len:
                sorted_list.extend(right[j:])
            
            return sorted_list
        
        return mergeSort(nums)