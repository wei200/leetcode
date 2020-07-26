class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        # same problem as 240 longest substring with at most K distinct characters, when K = 2 for this problem
        # Time: O(2N)
        # Space: O(1)
        max_length = 0
        window_start = 0
        freq = {}
        
        for window_end in range(len(tree)):
            
            right_fruit = tree[window_end]
            
            if right_fruit not in freq:
                freq[right_fruit] = 0
            freq[right_fruit] += 1
            
            while len(freq) > 2:
                left_fruit = tree[window_start]
                
                freq[left_fruit] -= 1
                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                window_start += 1
                
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
            
            
