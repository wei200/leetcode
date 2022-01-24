class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # rotation arrary, one half is in ascending order
        # binary search
        start = 0
        end = len(nums) -1
        while start <= end:
            
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            
            # left side is in ascending order
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # right side is sorted in ascending order
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        # the target is not found in the array
        return -1
                
                
        
