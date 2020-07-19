class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(2n)~ O(n), in the worst case, each char will be visited twice by start and end
        # Space: O(k), size for the sliding window
        #start and end of the window
        start = 0
        end = 0
        ans = 0
        chars = set()
        
        while start < len(s) and end < len(s):
            
            if s[end] not in chars:
                print(s[end])
                chars.add(s[end])
                print(chars)
                end += 1
                ans = max(ans, end - start)
            else:
                chars.remove(s[start])
                start += 1
        return ans
                    
                    
            
        
