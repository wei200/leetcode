class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ## Two pointers
        
        nums.sort()        
        count = 0
        for i in range(len(nums) - 2):
            count += self.search_pair(nums, target - nums[i], i)
        return count
    
    def search_pair(self,nums, target_sum, first):
            
        count = 0
        left = first + 1
        right = len(nums) - 1
            
        while left < right:   

            if nums[left] + nums[right] < target_sum: # found the target
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1
        return count
                
            
