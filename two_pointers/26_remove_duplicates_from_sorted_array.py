class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers, i and next_non_duplicate
        
        # i interate through the array
        # next_non_duplicate to place the next non_duplicate number
        
        # start from the second element
        next_non_duplicate = 1
        i = 1
        
        # iterate through the array
        while (i < len(nums)):
            if nums[next_non_duplicate - 1] != nums[i]:
                nums[next_non_duplicate] = nums[i]
                next_non_duplicate += 1
            i += 1
        return next_non_duplicate
        
        
        
