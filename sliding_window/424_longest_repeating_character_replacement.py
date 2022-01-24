class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # sliding window
        
        # Time: O(N)
        # Space: As we are expecting only the upper case letters in the input string, we can conclude that the space complexity will be O(26), 
        #to store each letterâs frequency in the HashMap, which is asymptotically equal to O(1).
        
        window_start = 0
        max_count = 0
        max_length = 0
        freq = {}
        
        # Try to extend the range [window_start, window_end]

        for window_end in range(len(s)):
            
            right_char = s[window_end]
            if right_char not in freq:
                freq[right_char] = 0
            freq[right_char] += 1
            max_count = max(max_count, freq[right_char])
            # Current window size is from window_start to window_end, overall we have a letter which is
            # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            if (window_end - window_start + 1 - max_count) > k:
                left_char = s[window_start]
                freq[left_char] -= 1
                window_start += 1
                
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
            
            
            
