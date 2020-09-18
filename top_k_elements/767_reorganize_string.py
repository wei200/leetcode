class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        # top k element pattern
        # use max heap
        
        
        freq = {}
        for char in S:
            freq[char] = freq.get(char, 0) + 1
            
        max_heap = []
        for char, frequency in freq.items():
            heappush(max_heap,(-frequency, char))
            
        previous_char = None
        previous_frequency = 0
        
        result = []
        
        while max_heap:
            frequency,char = heappop(max_heap)
            
            if previous_char and -previous_frequency > 0:
                heappush(max_heap, (previous_frequency, previous_char))
            result.append(char)
            previous_char = char
            previous_frequency = frequency + 1
            
        return ''.join(result) if len(result) == len(S) else ""
