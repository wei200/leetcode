class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        i = 0
        n = len(nums)
        while i < n:
            
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i += 1
                
        for i in range(n):
            if nums[i] != i + 1:
                return i+1
            
        return n + 1
       
