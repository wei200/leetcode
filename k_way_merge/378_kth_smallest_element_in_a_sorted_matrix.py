class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        
        # k-way merge pattern
        
        
        # push the first elemetns in a min heap
        min_heap = []
        for i in range(len(matrix)):
            heappush(min_heap,(matrix[i][0], 0, matrix[i]))
        
        count = 0
        number = 0
        while min_heap:
            number, i, row = heappop(min_heap)
            count += 1
            if count == k:
                break
            if len(row) > i + 1:   
                heappush(min_heap,(row[i+1],i+1,row))
        
        return number
    
    # another method is binary search
