# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        
        result = []
        queue = deque()
        queue.append(root)
        
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = deque()
            for _ in range(level_size):
                current_node = queue.popleft()
                
                if left_to_right:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
            result.append(current_level)
            left_to_right = not left_to_right
        
        return result
            
