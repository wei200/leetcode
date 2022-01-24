# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # BFS
        # O(N) visit each node
        # O(N) The space complexity of the above algorithm will be O(N)O(N) which is required for the queue.
        if root is None:
            return 0
        min_depth = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            min_depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right:
                    return min_depth
            
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
            
            
