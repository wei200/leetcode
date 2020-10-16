class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
#         # sol1: brute force, TLE
#         if n == 0:
#             return 1
        
#         if n == 1:
#             return 1
        
#         if n == 2:
#             return 2
        
#         take1Step = self.climbStairs(n - 1)
#         take2Step = self.climbStairs(n - 2)
        
#         return take1Step + take2Step
    
#     # sol2: top down dp (memoization)
#         dp = [0 for x in range(n+1)]
#         return self.climbStairs_recursive(dp,n)
    
#     def climbStairs_recursive(self, dp, n):
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         if dp[n] == 0:
#             take1Step = self.climbStairs_recursive(dp,n - 1)
#             take2Step = self.climbStairs_recursive(dp,n - 2)
            
#             dp[n] = take1Step + take2Step
        
#         return dp[n]

        # sol3: bottom-up dp
        
        if n == 0:
            return 1
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        dp = [0 for x in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
        # sol4: memoization optimization
        if n < 2:
            return 1
        if n == 2:
            return 2
        n1, n2 = 1,1
        for i in range(2,n+1):
            temp = n1+n2
            n1 = n2
            n2 = temp
        return n2
    

        

