class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       # subset questions
	# O(2^N)
	# O(2^N) 
        if nums is None:
            return None
        
        subsets = []
        # start by adding the empty subset
        subsets.append([])
        for currentNumber in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
            n = len(subsets)
            for i in range(n):
                # create a new subset from the existing subset and insert the current element to it
                set = list(subsets[i])
                set.append(currentNumber)
                subsets.append(set)

        return subsets
        
        
        
        
