class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list.sort(nums)
        
        result = []
        permutations = deque()
        permutations.append([])
        
        for cur_number in nums:
            
            n = len(permutations)
            
            for _ in range(n):
                old_permutations = permutations.popleft()
                
                for j in range(len(old_permutations)+1):

                    new_permutations = list(old_permutations)
                    new_permutations.insert(j, cur_number)
                    if len(new_permutations) == len(nums) and new_permutations not in result:
                        result.append(new_permutations)
                    else:
                         permutations.append(new_permutations)
        return result
                
                
