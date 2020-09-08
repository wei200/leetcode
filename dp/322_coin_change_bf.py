iimport math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Unbounded knapsack
        
        # brute force recursive solution
        # O(2^(N+c))
        # O(N+C) to store the recursion stack
        
        result = self.count_change_recursive(coins, amount, 0)
        if result == float("inf"):
            return -1
        else:
            return result
        
    
    def count_change_recursive(self, coins, amount, current_index):
        # base check
        if amount == 0:
            return 0
        
        n = len(coins)
        if n == 0 or current_index >= n:
            return float("inf")
        
        # recursive call after selecting the coin at the current_index
        count1 = float("inf")
        if coins[current_index] <= amount:
            res = self.count_change_recursive(coins, amount-coins[current_index], current_index)
            if res != -1:
                count1 = res + 1
            
        
        # recursive call after excluding the coin at the current index
        count2 = self.count_change_recursive(coins, amount, current_index + 1)
        
        return min(count1, count2)
                                                                  
                                                             
        
        
