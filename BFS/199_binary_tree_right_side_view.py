# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # BFS
        # append the last node of of each level
        if root is None:
            return root
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                # Or
                      # if i == levelSize - 1:
                      #   result.append(currentNode)
            result.append(current_level[-1])
        return result
                
