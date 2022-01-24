# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # Queue
        # OïNïsince traverse all the nodes in a tree
        # O(N) since the returned list has N elements
        
        if root is None:
            return root
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            current_level = []
            # the size of each level of the tree
            level_size = len(queue)
            # append level_size number of elemnts to each sub list
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
            # insert the child nodes current nodes
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            # append the sublist
            result.append(current_level)
            
        return result
                
                
        
