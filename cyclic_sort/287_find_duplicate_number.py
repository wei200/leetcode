class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # cyclic sort
        # O(N)
        # O(1)
        
        i = 0
        while i < range(len(nums)):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[j] != nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        

