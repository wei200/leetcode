class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Sliding Window
        # Time: O(N + N) -> O(N), each element may be visited at most twice, so 2N
        # Space: O(1), only constant space for min_length, window_start, window_end

        min_length = float("inf")
        window_start = 0
        window_sum = 0.0
        
        for window_end in range(len(nums)):
            
            window_sum += nums[window_end]
            
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
                
        if min_length == float("inf"):
            return 0
        return min_length
            
            
            
        
