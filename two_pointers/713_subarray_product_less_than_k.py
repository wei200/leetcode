class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Two pointers/sliding windwo
        # O(N)
        # O(1)
        
        count = 0
        product = 1
        left = 0
        
        if k  <= 1:
            return 0
        for right in range(len(nums)):
            
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            print(right-left+1)    
            count += right - left + 1
                
            
        return count
            
               
