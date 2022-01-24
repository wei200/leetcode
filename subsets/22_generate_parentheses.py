class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # use permutation pattern
        
        result = []
        
        queue = deque()
        queue.append("")
        
        while queue:
            
            ps = queue.popleft()
            
            if ps.count('(') == n and ps.count(')') == n:
                result.append(ps)
                
            else:
                
                if ps.count('(') < n:
                    queue.append(ps + "(")
                if ps.count('(') > ps.count(')'):
                    queue.append(ps+")")
                                          
        return result
