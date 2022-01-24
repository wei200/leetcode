class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # Merge intervals
        # O(NlogN)
        # O(N) as we need to return a list containing all the merged intervals. We will also need O(N)O(N) space for sorting.
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        
        mergedIntervals = []
        start = intervals[0][0]
        end = intervals[0][-1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[-1], end)
                
            else:
                
                mergedIntervals.append([start,end])
                start = interval[0]
                end = interval[-1]
                
        mergedIntervals.append([start,end])       
        return mergedIntervals
        
