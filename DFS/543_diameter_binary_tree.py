# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree_depth = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_depth(root)
        return self.tree_depth
 
    def find_depth(self,current_node):
        
        # it's a leaf node
        if current_node is None:
            return 0
            
        left_tree_height = self.find_depth(current_node.left)
        right_tree_height = self.find_depth(current_node.right)
        
        depth = left_tree_height + right_tree_height
        # update the global tree depth
        self.tree_depth = max(self.tree_depth, depth)
        
        # The height of the current node will be equal to the maximum of the heights of its left or right children, plus â1â for the current node.
        return max(left_tree_height,right_tree_height) + 1
 

