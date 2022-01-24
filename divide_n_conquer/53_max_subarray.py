class Solution(object):
    # Time: O(nlogn)
    # Space: O(logN)
    
    # caculate the cross sum
    def maxCrossSum(self,nums,l,r,m):
        
        sm = 0
        left_sum = -10000
        # caculate the left sum
        for i in range(m, l - 1, -1):
            sm += nums[i]
            left_sum = max(left_sum,sm)
                
       # calculate the right sum 
        sm = 0
        right_sum = -10000
        for i in range(m + 1, r + 1):
            sm += nums[i]
            right_sum = max(right_sum, sm)
        
        # return the cross sum
        return left_sum + right_sum
    
    
    def helper(self, nums, l, r):
        # if only one element
        if l == r:
            return nums[l]
        
        m = (l + r) // 2
        
        # caculate the left sum and right sum recursively
        left_sum = self.helper(nums, l, m)
        right_sum = self.helper(nums, m + 1, r)
        cross_sum = self.maxCrossSum(nums, l, r, m)
        
        return max(left_sum, right_sum, cross_sum)
            
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.helper(nums, 0, len(nums) - 1)
    
    
