class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Two pointers
        
        # Time: O(N^2 + NlogN)
        # Space: O(N) for sorting
        
        nums.sort()
        
        smallest_difference = float("inf")
        
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target_diff = target - nums[left] - nums[right] - nums[i]
                if target_diff == 0: # find the exact triplets
                    return target - target_diff
            
            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            # if we don't have exact sum, we will compare absolute values between target_diff and abs(smalleset_difference)
            # we'll take it in two cases, first case when abs(target_diff) < abs(smallest_diff)
            # second, when absolute vales are equal, and but the sign are opposite
                if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                    smallest_difference = target_diff
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        # smallest_difference + triplets_sum = target      
        return target - smallest_difference
        
