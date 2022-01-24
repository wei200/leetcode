class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Time complexity: O(N*N!)
        # Space: O(N*N!)
        result = []
        permutations = deque()
        permutations.append([])
        
        for curr_number in nums:
            
            n = len(permutations)
            
            for _ in range(n):
                # ååºpermutationéæäªçåïæå[[1,3],[3,1]],åéåºæ¥[1ï3]ïç¶åéåº[3ï1]ïåèè5çæå¥
                old_permutations = permutations.popleft()
                
                for j in range(len(old_permutations) + 1):
                    new_permutations = list(old_permutations)
                    # at jth index, insert curr_number
                    new_permutations.insert(j, curr_number)
                    
                    # if the length = nums length, means found one possible permutation, add it to the result
                    if len(new_permutations) == len(nums):
                        result.append(new_permutations)
                    # else, keep the current perm and save it for next round
                    else:
                        permutations.append(new_permutations)
        return result
