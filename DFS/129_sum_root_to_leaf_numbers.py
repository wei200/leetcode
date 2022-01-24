# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # DFS
        # O(N) traverse each node once
        # O(N) store the recursion stack, the worst case happen when the given tree is a linked list (i.e. every node has only one child)
        if root is None:
            return 0
        
        return self.find_root_to_leaf_path_number(root, 0)
        
    def find_root_to_leaf_path_number(self, current_node, path_sum):
        
        if current_node is None:
            return 0
        
        path_sum = 10 * path_sum + current_node.val
        
        # if the current node is a leaf, return the current path sum
        if current_node.left is None and current_node.right is None:
            return path_sum
        
        return self.find_root_to_leaf_path_number(current_node.left, path_sum) + self.find_root_to_leaf_path_number(current_node.right,path_sum)
    
    
        
        
