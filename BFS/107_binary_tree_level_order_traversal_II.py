# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # queue
        # O(N)
        # O(N) since the returned result queue has N element and also queue needs N elemetns
        if root is None:
            return root
        
        queue = deque()
        queue.append(root)
        
        result = deque()
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                
                
            result.appendleft(current_level)
        return result
            
            
