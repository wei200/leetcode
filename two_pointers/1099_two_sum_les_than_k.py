class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        # two pointers
        A.sort()
        left = 0
        right = len(A) - 1
        max_sum = -1
        while left < right:
            if A[left] + A[right] < K:
                max_sum = max(max_sum,A[left] + A[right])
                left += 1
            else:
                right -= 1
        return max_sum
                
