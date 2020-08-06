class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        slow = n
        fast = n
        while True:
            slow = self.find_square_sum(n) # move one step
            fast = self.find_square_sum(self.find_square_sum(n)) # move two steps
            if slow == fast: # found the cycle
                break
        return slow == 1 # see if the cycle is stuck on number 1
        
    def find_square_sum(self, n):
        
        _sum = 0
        while (n > 0):
            digit = n % 10
            _sum += digit ** 2
            n = n // 10
            
        return _sum
        :
