class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # cyclic sort approach
        
        # duplicates don't matter, still apply the cyclic sort appoach and the duplicates will be eventually placed on the wrong index and will still be indentified
        
        i = 0
        missing_number = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_number.append(i + 1)
        
        return missing_number
