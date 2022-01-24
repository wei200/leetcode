import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS
        # O(N) since we traverse each node once
        # O(N) in the worst case the given tree is a linked list (i.e. every tree has only one child)
        
        self.global_max_sum = -float("inf")
        self.find_max_path_sum(root)
        return self.global_max_sum
        
    def find_max_path_sum(self, current_node):
        if current_node is None:
            return 0
        
        left_sum = self.find_max_path_sum(current_node.left)
        right_sum = self.find_max_path_sum(current_node.right)
        
        # ignore paths with negative sums since we need to find the max sum
        left_sum = max(left_sum,0)
        right_sum = max(right_sum,0)
        total = left_sum + right_sum + current_node.val
        
        self.global_max_sum = max(self.global_max_sum, total)
        
        return max(left_sum, right_sum) + current_node.val
