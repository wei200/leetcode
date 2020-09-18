class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # bottom-up tabulation
        
        n = len(coins)
        dp = [[float("inf") for _ in range(amount+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
            
        for i in range(n):
            for t in range(1, amount+1):
                # exlude the coin
                dp[i][t] = dp[i-1][t]
                # include the coin
                if coins[i] <= t:
                    if dp[i][t-coins[i]] != float("inf"):
                        
                        # include the coin, dp[i][t] is the case that excludes the coin
                        dp[i][t] = min(dp[i][t],dp[i][t-coins[i]]+1)
        # total combination will be at the bottom right corner
        if dp[n-1][amount] == float("inf"):
            return -1
        else:
            return dp[n-1][amount]
                        
                
#         # Unbounded knapsack
#         # top-down memoization
#         # O(C*T)
#         # O(C*T)
#         dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
#         result = self.count_change_recursive(dp, coins, amount, 0)
#         if result == float("inf"):
#             return -1
#         else:
#             return result
        
#     def count_change_recursive(self, dp, coins, amount, current_index):
#         # base check
#         if amount == 0:
#             return 0
            
#         n = len(coins)
#         if n == 0 or current_index >= n:
#             return float("inf")
            
#         # check if we have not already processed a similar sub-problem
#         if dp[current_index][amount] == -1:
#             # include the coin at the current index
#             count1 = float("inf")
#             if coins[current_index] <= amount:
#                 res = self.count_change_recursive(dp, coins, amount-coins[current_index], current_index)
#                 if res != float("inf"):
#                     count1 = res + 1
                        
#             # exclude the coin at the current_index
#             count2 = self.count_change_recursive(dp, coins, amount, current_index+1)
#             dp[current_index][amount] = min(count1,count2)
            
#         return dp[current_index][amount]
    
        
        
                        
                                                             
        
        
