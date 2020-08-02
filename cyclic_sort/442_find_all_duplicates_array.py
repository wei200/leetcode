class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # cyclic sort approach
        
        # O(N)
        # O(1)
        
        i = 0
        duplicate_number = []
        while i < len(nums):
            # nums[i] are supposed to be at jth index
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate_number.append(nums[i])
        
        return duplicate_number
            
        
