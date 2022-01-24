class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #O(2^N)
        #O(2^N)
        list.sort(nums)
        
        # start with empty subset
        subsets = []
        subsets.append([])
        
        start_ind = 0
        end_ind = 0
        
        # add each element nums[i]
        for i in range(len(nums)):
            # start index
            start_ind = 0
            # if the new elements is the same as the previous elements, start_ind starts in the middle
            if i > 0 and nums[i] == nums[i - 1]:
                start_ind = end_ind + 1
            # end index  
            end_ind = len(subsets) - 1
            
            for j in range(start_ind, end_ind + 1):
                set = list(subsets[j])
                set.append(nums[i])
                subsets.append(set)
            
        return subsets
        
