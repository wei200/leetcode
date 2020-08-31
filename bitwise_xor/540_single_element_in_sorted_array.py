class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # XOR
        # O(n) since we interate through all numbers of input array
        # O(1) 
#         Recall the following two properties of XOR:

# It returns zero if we take XOR of two same numbers.
# It returns the same number if we XOR with zero.
        num = 0
        for i in nums:
            num ^= i
        
        return num
            
        
        
