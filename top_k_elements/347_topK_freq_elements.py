class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # top k pattern
        # use min-heap + hash map
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        min_heap = []
        for num, freq in freq.items():
            heappush(min_heap,(freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
        
        # create a list of top k numbers
        top_numbers = []
        while min_heap:
            top_numbers.append(heappop(min_heap)[1])
        
        return top_numbers
        
