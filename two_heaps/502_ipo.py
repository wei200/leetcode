class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        
        # two heaps
        
        min_heap_capital = []
        max_heap_profit = []
        
        for i in range(len(Capital)):
            heappush(min_heap_capital,(Capital[i],i))
        
        print(min_heap_capital)
        
        available_capital = W # inital capital
        for _ in range(k):
            
            #find all projects that can be selected within the available capital and insert them into a max heap
            while min_heap_capital and min_heap_capital[0][0] <= available_capital:
                capital, i = heappop(min_heap_capital)
                heappush(max_heap_profit, (-Profits[i],i))
                
            # terminate if we can't find any project that can be invested within the avail capital
            if not max_heap_profit:
                break
                    
            available_capital += -heappop(max_heap_profit)[0]
                
        return available_capital
                    
                    
        
