class KthLargest(object):
    min_heap = []

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heappush(self.min_heap,val)
        
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]
        
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
