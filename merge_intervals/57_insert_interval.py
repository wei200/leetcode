class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # O(N)
        # O(N)
        
        merged = []
        i = 0
        start, end = 0, 1
        
        # skip all intervals that come before the start of the new interval and add those to output
        
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
        
        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start],newInterval[start])
            newInterval[end] = max(intervals[i][end],newInterval[end])
            i += 1
        
        merged.append(newInterval)
        
        #add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
