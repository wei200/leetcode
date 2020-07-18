class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        # Time: O(N2)
        # Space: O(1)
        # for i in range(0, len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target and j != i:
        #             return [i,j]
        
# use hashmap (dictionary in Python),  look back to check if current element's #complement already exists in the table. If it exists, we have found a solution # and return immediately.
# store num:index in the dict
# Time: O(N)
# Space: O(N) store at most N elements in dict
        h = {}
        for ind, val in enumerate(nums):
            n = target - val
            if n not in h:
                h[val] = ind
            else:
                return [h[n], ind]
