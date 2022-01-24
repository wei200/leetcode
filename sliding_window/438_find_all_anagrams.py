class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # sliding window
        
        # save the letter and occurance in the hashmap
        freq = {}
        start = 0
        for char in p:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        # use a list to store the starting index
        
        result = []
        start = 0
        matched = 0
        
        for end in range(len(s)):
            
            right_char = s[end]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] == 0:
                    matched += 1
                    
            if matched == len(freq):
                print(matched,len(freq))
                result.append(start)
                
            
            if end >= len(p) - 1:
                left_char = s[start]
                if left_char in freq:
                    if freq[left_char] == 0:
                        matched -= 1
                    freq[left_char] += 1
                start += 1

        return result
                    
                    
      
