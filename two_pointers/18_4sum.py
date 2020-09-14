class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        
        # Two pointers
        # sorting takes O(NlogN), overall takes N^3 + NlogN, ~O(N^3)
        # O(N) for sorting
        
        nums.sort()
        quad = []
        
        for i in range(len(nums)-3):
            # for A,B,C,D, check if A is equal to B, skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # for A,B,C,D, check if B is equal to C
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                self.search_pair(nums,target,i,j,quad)
        return quad
       
    def search_pair(self,nums,target_sum,first,second,quad):
        left = second + 1
        right = len(nums) - 1
        while (left < right):
            s = nums[first] + nums[second] + nums[left] + nums[right]
            if s == target_sum:
                quad.append([nums[first],nums[second],nums[left],nums[right]])
                left += 1
                right -= 1
                # skip same elemetn to avoid duplicates
                while (left < right and nums[left] == nums[left-1]):
                    left += 1
                while (left < right and nums[right] == nums[right+1]):
                    right -= 1
            elif s < target_sum:
                left += 1
            else:
                right -= 1
            

        
