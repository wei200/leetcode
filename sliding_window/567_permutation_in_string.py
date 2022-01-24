class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # Sliding window, hashmap
        # Time: O(N)
        # Space: O(len(s1)), maintain the hashmap
        
        freq = {}
        for char in s1:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        window_start = 0
        matched = 0
        
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] == 0:
                    matched += 1
            
            if matched == len(freq):
                return True
            
            # shrink the window
            
            if window_end + 1 >= len(s1):
                left_char = s2[window_start]
                if left_char in freq:
                    if freq[left_char] == 0:
                        matched -= 1
                    freq[left_char] += 1
                
                window_start += 1
                
        return False
            
            
