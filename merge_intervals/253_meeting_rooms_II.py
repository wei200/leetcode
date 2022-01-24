class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # use min heap based on meeting.endtime
        # the heap will always have overlapping meetings
        # O(NlogN)
        # O(N)
        intervals.sort(key=lambda x:x[0])
        
        min_rooms = 0
        min_heap = []
        for meeting in intervals:
            while(len(min_heap)) > 0 and meeting[0] >= min_heap[0]:
                heappop(min_heap)
            heappush(min_heap,meeting[1])
            min_rooms = max(min_rooms,len(min_heap))
        return min_rooms
            
