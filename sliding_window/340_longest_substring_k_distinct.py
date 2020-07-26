class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # O(N)
        # O(K), store K characters in hashmap
        # Sliding window
        max_length = 0
        freq = {}
        window_start = 0
        
        if k == 0:
            return k
        
        for window_end in range(len(s)):
            
            right_char = s[window_end]
            if right_char not in freq:
                freq[right_char] = 0
            freq[right_char] += 1
            
            while len(freq) > k:
                # shrink the window
                left_char = s[window_start]
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    #delete this key
                    del freq[left_char]
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
            
