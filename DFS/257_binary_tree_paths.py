# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # DFS
        # O(N)
        
        if root is None:
            return root
        all_paths = []
        self.find_tree_path(root,"",all_paths)
        return all_paths
        
    def find_tree_path(self, current_node, path,all_paths):
        
        if current_node is None:
            return
        
        path = path + str(current_node.val) + '->'
        
        if current_node.left is None and current_node.right is None:
            path = path[:-2]
            all_paths.append(path)
        
        else:
            self.find_tree_path(current_node.left,path,all_paths) 
            self.find_tree_path(current_node.right,path,all_paths)
        
            
        
