class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
#         # sol1: brute force
#         return min(self.find_min_cost_recursive(cost,0),self.find_min_cost_recursive(cost,1))
    
#     def find_min_cost_recursive(self,cost,current_index):
#         n = len(cost)
#         if current_index > n - 1:
#             return 0
        
#         # if take 1 step, we are left with n-1 steps
#         take1Step = self.find_min_cost_recursive(cost,current_index+1)
        
#         # if take 2 step, left with n-2 steps
#         take2Step = self.find_min_cost_recursive(cost,current_index+2)
        
#         min_cost = min(take1Step,take2Step)
#         return min_cost + cost[current_index]

#         # sol2: top down memoization
#         dp = [0 for x in range(len(cost))]
#         return min(self.find_min_cost_recursive(dp,cost,0),self.find_min_cost_recursive(dp,cost,1))
    
#     def find_min_cost_recursive(self,dp,cost,current_index):
#         n = len(cost)
#         if current_index > n - 1:
#             return 0
#         if dp[current_index] == 0:
#             take1Step = self.find_min_cost_recursive(dp,cost,current_index+1)
#             take2Step = self.find_min_cost_recursive(dp,cost,current_index+2)
#             dp[current_index] = cost[current_index] + min(take1Step, take2Step)
            
#         return dp[current_index]
        
        # sol3: bottom up dp
        # not completed
        
        n = len(cost)
        dp = [0 for x in range(n+1)]
        dp[0] = 0 # no steps, no need to pay
        dp[1] = cost[0] # 1 step, we have to pay its fee
        dp[2] = cost[0] # one more step reach to the top after 1st step, no need to pay
        
        for i in range(2,n+1):
            dp[i+1] = min(cost[i]+dp[i],cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        
        return dp[n]
        
    
