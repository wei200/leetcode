class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # Time: O(N*2**N), 2**N permutations, and for each permutation, concecatnate the strings using .join(), which takes O(N), so total is N*2**N
        # Space:
        
        permutations = []
        permutations.append(S)
        
        for i in range(len(S)):
            if S[i].isalpha(): # only process letters, skip digits
                
                n = len(permutations)
                
                for j in range(n):
                    
                    chs = list(permutations[j])
                    chs[i] = chs[i].swapcase()
                    permutations.append(''.join(chs))
                    
        return permutations
