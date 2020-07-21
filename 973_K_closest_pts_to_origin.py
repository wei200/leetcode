class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        ## brute force
        # O(NlogN)
        # O(N)
        # points.sort(key = lambda P: P[0] ** 2 + P[1] ** 2)
        # return points[:K]
        
        
        # use heap (data struture to represent priority queue)
        # heapq from python is built on min heap
        # Time: O(Nlogk), each insertionInserting an item to a heap of size k take O(logK) time.
        # And we do this for each item points.
        #So runtime is O(N * logK) where N is the length of points.

        #Space: O(K) for our heap.
        
        heap = []
        
        for (x,y) in points:
            print(heap)
            dist = -(x ** 2 + y ** 2)

            heapq.heappush(heap, (dist, x, y))
            
            if len(heap) > K:
                heapq.heappop(heap)
                
        return [(x,y) for (dist, x, y) in heap]

