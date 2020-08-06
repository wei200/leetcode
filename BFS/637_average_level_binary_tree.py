# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        # BFS
        
        if root is None:
            return root
        
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            sum_level = 0.0
            for _ in range(len(queue)):
                current_node = queue.popleft()
                sum_level += current_node.val
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
            result.append(sum_level/level_size)
        return result

