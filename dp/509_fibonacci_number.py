class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # brute force recursive solution
        
#         if N == 0 or N == 1:
#             return N
        
#         return self.fib(N-1) + self.fib(N-2)
    
        
        # memoization

        # memo = {0:0,1:1}
        # if N in memo.keys():
        #     return memo[N]
        # else:
        #     memo[N] =self.fib(N-1) + self.fib(N-2)
        #     return memo[N]
        
        # bottom up
        # O(n)
        # O(N)
        # if N < 2:
        #     return N
        # dp = [0,1]
        # for i in range(2,N+1):
        #     dp.append(dp[i-1]+dp[i-2])
        # return dp[N]
    
    # memory improved bottom up
        if N < 2:
            return N
        n1,n2,temp = 0,1,0
        for i in range(2,N+1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    
        
        
