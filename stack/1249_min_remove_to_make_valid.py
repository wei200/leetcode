class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two step
        # 1. Identify all indexes that should be removed.
        # 2. Build a new string with removed indexes.
        
        
        # Time complexity: O(N)
        # Space complexity: O(N), We are using a stack, set, and string builder, 
        # each of which could have up to n characters in them, and so require up to O(N) space.
        
        # the index of the elements to be removed
        # use this set to keep track of the unmathced )
        indexes_to_remove = set()
        
        # initialize a stack
        stack = []
        
        # loop over s and find the indexe to be removed
        for i, c in enumerate(s):
            
            # if element is not a bracket, i.e. is a number, skip this iteration
            if c not in "()":
                continue
            # if elemetn is an opening bracket, add the index i to stack
            if c == '(':
                stack.append(i)
                
            # if stack is already empty, this bracket is redudant and needs to be removed later,
            # so we write down the index of it
            elif not stack:
                
                indexes_to_remove.add(i)
            # the element finds a pair with exisiting (
            else:
                stack.pop()
                
        indexes_to_remove = indexes_to_remove.union(set(stack))
        
        string_builder = [ ]
        
        # loop over s again and add desired elements into a string_builder list
        for i, c in enumerate(s):
            
            if i not in indexes_to_remove:
                
                string_builder.append(c)
                
        return "".join(string_builder)
