        heap = []
        
        for (x,y) in points:
            #print(heap)
            dist = -(x ** 2 + y ** 2)

            heapq.heappush(heap, (dist, x, y))
            
            if len(heap) > K:
                heapq.heappop(heap)
                
        return [(x,y) for (dist, x, y) in heap]
