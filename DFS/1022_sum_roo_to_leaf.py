# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.find_path(root, 0)
    
    
    def find_path(self, current_node, path_sum):
        
        if current_node is None:
            return 0
        
        path_sum = 10 * path_sum + current_node.val
        
        if current_node.left is None and current_node.right is None:
            return int(str(path_sum),2)
        
        # traverse the left and right sub-trees
        
        return self.find_path(current_node.left, path_sum) + self.find_path(current_node.right,path_sum)
