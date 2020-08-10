class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # modified binary search
        
        # O(logN)
        # O(1)
        
        
        result = [-1,-1]
        result[0] = self.binary_search(nums,target,False)
        if result[0] != -1:
            result[1] = self.binary_search(nums,target,True)
        
        return result
        
    def binary_search(self, nums, target, find_max_index):
            
        start = 0
        end = len(nums) - 1
        target_index = -1
        while start <= end:
            # use binary search to first find the key (i.e. key=nums[mid])
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                target_index = mid
                # search behind to find the last index of 'key'
                if find_max_index:
                    start = mid + 1

                else: # search ahead to find the first index of key
                    end = mid  - 1
            
        return target_index

            
            
            
        
