class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        
        # O(NlogN) insert elemetn into the heap
        # O(N) space to ropes in the heap
        min_heap = []
        for i in sticks:
            heappush(min_heap,i)
        cost = 0
        while len(min_heap) > 1:
            temp = heappop(min_heap) + heappop(min_heap)
            cost += temp
            heappush(min_heap, temp)
        return cost
