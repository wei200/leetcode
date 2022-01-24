class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # cyclic sort
    # O(N)
    # O(1)
        i = 0
        n = len(nums)
        
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        # find the number missing from its index
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
        
