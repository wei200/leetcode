class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # sort
        # Time: O(NlogN)
        # Space: O(1)
        # sorted in python return in ascending order
        
        #return sorted(nums)[-k]
    
    
        # heap
        # add k elements to a heap is O(klogN)
        # Space: O(k), save the heap
        return heapq.nlargest(k, nums)[-1]
        
        
    
        
