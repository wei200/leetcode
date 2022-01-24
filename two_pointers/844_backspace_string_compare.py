class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        
        # work in reverse order, so we can apply backspace
        
        index1 = len(S) - 1
        index2 = len(T) - 1
        
        while (index1 >= 0 or index2 >= 0):
            
            i1 = self.next_valid_index(S,index1)
            i2 = self.next_valid_index(T,index2)
            
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if S[i1] != T[i2]:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
            
            
        return True
            

            

    def next_valid_index(self,str,index):
        
        backspace_count  = 0
        while (index >= 0):
            if str[index] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
                
            index -= 1
        
        return index
        
