# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        all_paths = []
        self.find_paths_recursive(root, sum, [],all_paths)
        return all_paths
        
    
    def find_paths_recursive(self,current_node, required_sum, current_path, all_paths):
        
        if current_node is None:
            return
        
        current_path.append(current_node.val)

        if current_node.val == required_sum and current_node.left is None and current_node.right is None:
            all_paths.append(list(current_path))
            
        else:
            
            # traverse the left sub-tree
            self.find_paths_recursive(current_node.left, required_sum - current_node.val, current_path, all_paths)
            
            # traverse the right sub-tree
            self.find_paths_recursive(current_node.right, required_sum - current_node.val, current_path, all_paths)
            
            # we need to remove the current node while we're going up the recursive call stack
        del current_path[-1]
