# time complexity: O(n), access each element once in the loop
# space complexity: O(n), in the worst case, no closing bracket, push all the opening brackets to the stack, e.g. {[{[(((((((
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = [ ]
        # hash map
        mapping = {")":"(", "}":"{", "]":"["}
        
        # for each element in s
        for char in s:
            
            # if char is an closing bracket
            
            if char in mapping:
                
                # Pop the topmost element from stack, if it's not an empty stack, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
                
            else:
                
                stack.append(char)
                
        # in the end, if the stack is empty, means it's a valid expression.
        return not stack
                
