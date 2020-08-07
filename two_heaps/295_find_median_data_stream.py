class MedianFinder(object):
    


    def __init__(self):
        """
        initialize your data structure here.
        """

        self.max_heap =[]
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        
        else:
            heappush(self.min_heap, num)
            
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0

        return -self.max_heap[0] / 1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian():
