# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
        return self.find_path_recursive(root, arr, 0)
    
    def find_path_recursive(self, current_node, arr, arr_index):
        
        if current_node is None:
            return False
        
        arr_len = len(arr)
        # if the length of the array is greater than the length from root to path or current value does not match value in the array
        if arr_index >= arr_len or current_node.val != arr[arr_index]:
            return False
        
        # if the current node is a leaf
        if current_node.left is None and current_node.right is None and arr_index == arr_len - 1:
            return True
        
        # traverse the left and right child nodes
        return self.find_path_recursive(current_node.left, arr, arr_index + 1) or self.find_path_recursive(current_node.right, arr, arr_index + 1)
    
