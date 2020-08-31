class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        # binary search + min_heap (top k)
        
        index = self.binary_search(arr,x)
        low, high = index -k, index + k
        
        low = max(low,0)
        high = min(high,len(arr)-1)
        
        min_heap = []
        # add all elements to the heap, sorted by the abs diff
        for i in range(low, high + 1):
            heappush(min_heap, (abs(arr[i] - x), arr[i]))
            
        result = []
        for _ in range(k):
            result.append(heappop(min_heap)[1])
        
        result.sort()
        return result
    
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > 0:
            return low - 1
        return low
        
        
