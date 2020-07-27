class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Two pointer
        # Time: O(N)
        # Space: O(1)
        next_element = 0
        
        for i in range(len(nums)):
            
            if nums[i] != val:
                nums[next_element] = nums[i]
                next_element += 1
        
        return next_element
                
                
        
        
