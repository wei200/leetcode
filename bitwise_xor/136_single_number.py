class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # bitwise XOR
        # O(N)
        #O(1)
        
        num = 0
        for i in nums:
            num ^= i
        return num
       
